import ast
import re
import json
import requests
from django.contrib.gis.gdal import SpatialReference
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.gis.geos import GEOSGeometry, GeometryCollection
from hyper_resource.contexts import *
from rest_framework.negotiation import BaseContentNegotiation
from django.contrib.gis.db import models

class IgnoreClientContentNegotiation(BaseContentNegotiation):
    def select_parser(self, request, parsers):
        """
        Select the first parser in the `.parser_classes` list.
        """
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):
        """
        Select the first renderer in the `.renderer_classes` list.
        """
        return (renderers[0], renderers[0].media_type)

class AbstractResource(APIView):

    def __init__(self):
        super(AbstractResource, self).__init__()
        self.context_resource = None
        self.initialize_context()
        self.current_object_state = None
        self.object_model = None

    content_negotiation_class = IgnoreClientContentNegotiation

    def initialize_context(self):
        return ContextResource()

    def _base_path(self, full_path):
        arr = full_path.split('/')
        ind = arr.index(self.contextclassname)
        return '/'.join(arr[:ind+1])

    def _set_context_to_model(self):
        self.context_resource.contextModel(self.object_model)

    def _set_context_to_attributes(self, attribute_name_array):
        self.context_resource.set_context_to_attributes(attribute_name_array)

    def _set_context_to_object(self, attribute_name):

        self.context_resource.set_context_to_object(self.current_object_state, attribute_name)

    def set_context_resource(self, request ):
        self.context_resource.model = object
        self.context_resource.host = request.META['HTTP_HOST']
        self.context_resource.basic_path = self._base_path(request.META['PATH_INFO'])

    def model_class(self):
        return self.serializer_class.Meta.model

    def key_is_identifier(self, key):
        return key in self.serializer_class.Meta.identifiers

    def dic_with_only_identitier_field(self, dict_params):
        dic = dict_params.copy()
        a_dict = {}
        for key, value in dic.items():
            if self.key_is_identifier(key):
                a_dict[key] = value

        return a_dict

    def attributes_functions_name_template(self):
        return 'attributes_functions'

    def get_object(self, a_dict):
        dicti = self.dic_with_only_identitier_field(a_dict)
        queryset = self.model_class().objects.all()
        obj = get_object_or_404(queryset, **dicti)
        #self.check_object_permissions(self.request, obj)
        return obj

    def operation_names_model(self):
        return self.object_model.operation_names()

    def attribute_names_model(self):
        return self.object_model.attribute_names()
    
    def is_private(self, attribute_or_method_name):
        return attribute_or_method_name.startswith('__') and attribute_or_method_name.endswith('__')

    def is_not_private(self, attribute_or_method_name):
        return not self.is_private(attribute_or_method_name)

    def is_operation(self, operation_name):
        return operation_name in self.operation_names()

    def is_attribute(self, attribute_name):
        return attribute_name in dir(self) and not callable(getattr(self, attribute_name))

    def _has_method(self,  method_name):
        return hasattr(self.object_model, method_name) and callable(getattr(self.object_model, method_name))

    def has_only_attribute(self,  attributes_functions_name):
        attrs_functs = attributes_functions_name.split('/')
        if len(attrs_functs) > 1:
            return False
        if ',' in attrs_functs[0]:
            return True
        if self._has_method(attrs_functs[0]):
            return False
        return hasattr(self.object_model, attrs_functs[0])

    def attributes_functions_splitted_by_url(self, attributes_functions_str_url):
        res = attributes_functions_str_url.lower().find('http:')
        if res == -1:
            res = attributes_functions_str_url.lower().find('https:')
            if res == -1:
                res = attributes_functions_str_url.lower().find('www.')
                if res == -1:
                    return [attributes_functions_str_url]

        return [attributes_functions_str_url[0:res], attributes_functions_str_url[res:]]

    def attributes_functions_str_has_url(self, attributes_functions_str_url):
        return (attributes_functions_str_url.find('http:') > -1) or (attributes_functions_str_url.find('https:') > -1)\
               or (attributes_functions_str_url.find('www.') > -1)

    def _execute_attribute_or_method(self, object, attribute_or_method_name, array_of_attribute_or_method_name):

        dic = {}
        parameters = []
        arr_attrib_method_name = array_of_attribute_or_method_name
        att_or_method_name = attribute_or_method_name

        if self.is_operation_and_has_parameters(att_or_method_name):
            parameters = arr_attrib_method_name[0].split('&')
            arr_attrib_method_name = arr_attrib_method_name[1:]

        obj = self._value_from_object(object, att_or_method_name, parameters)

        if len(arr_attrib_method_name) == 0:
            return obj

        return self._execute_attribute_or_method(obj, arr_attrib_method_name[0], arr_attrib_method_name[1:])

    def is_operation_and_has_parameters(self, attribute_or_method_name):
        dic = self.operations_with_parameters_type()
        return (attribute_or_method_name in dic) and len(dic[attribute_or_method_name])

    def function_name(self, attributes_functions_str):
        functions_dic = self.operations_with_parameters_type()
        if str(attributes_functions_str[-1]) in functions_dic:
            return str(attributes_functions_str[-1])
        return str(attributes_functions_str[-2])

class SpatialResource(AbstractResource):

    def get_geometry_object(self, object_model):
        return getattr(object_model, self.geometry_field_name(), None)

    def geometry_field_name(self):
        return self.serializer_class.Meta.geo_field

    def make_geometrycollection_from_featurecollection(self, feature_collection):
        geoms = []
        features = ast.literal_eval(feature_collection)
        for feature in features['features']:
            feature_geom = feature['geometry']
            geoms.append(GEOSGeometry(feature_geom))
        return GeometryCollection(tuple(geoms))

    def all_parameters_converted(self, attribute_or_function_name, parameters):
        parameters_converted = []
        if self.is_operation_and_has_parameters(attribute_or_function_name):
            parameters_type = self.operations_with_parameters_type()[attribute_or_function_name]
            for i in range(0, len(parameters)):
                if GEOSGeometry == parameters_type[i]:
                    geometry_dict = json.loads(parameters[i])
                    if isinstance(geometry_dict, dict) and geometry_dict['type'].lower() == 'feature':
                        parameters_converted.append(parameters_type[i](json.dumps(geometry_dict['geometry'])))
                    elif isinstance(geometry_dict, dict) and geometry_dict['type'].lower() == 'featurecollection':
                        geometry_collection = self.make_geometrycollection_from_featurecollection(parameters[i])
                        parameters_converted.append(parameters_type[i](geometry_collection))
                    else:
                        parameters_converted.append(parameters_type[i](parameters[i]))
                else:
                    parameters_converted.append(parameters_type[i](parameters[i]))


            return parameters_converted

        return self.parametersConverted(parameters)

    def _value_from_object(self, object, attribute_or_function_name, parameters):

        if len(parameters):
            params = self.all_parameters_converted(attribute_or_function_name, parameters)
            return getattr(object, attribute_or_function_name)(*params)

        return getattr(object, attribute_or_function_name)

    def parametersConverted(self, params_as_array):
        paramsConveted = []

        for value in params_as_array:
            if value.lower() == 'true':
                paramsConveted.append(True)
                continue
            elif value.lower() == 'false':
                paramsConveted.append(False)
                continue

            try:
                paramsConveted.append(int( value ) )
                continue
            except ValueError:
                pass
            try:
               paramsConveted.append( float( value ) )
               continue
            except ValueError:
                pass
            try:
               paramsConveted.append( GEOSGeometry( value ) )
               continue
            except ValueError:
                pass
            try:
                http_str = (value[0:4]).lower()
                if (http_str == 'http'):
                    resp = requests.get(value)
                    if 400 <= resp.status_code <= 599:
                        raise HTTPError({resp.status_code: resp.reason})
                    js = resp.json()

                    if (js.get("type") and js["type"].lower() in ['feature', 'featurecollection']):
                        a_geom = js["geometry"]
                    else:
                        a_geom = js
                    paramsConveted.append(GEOSGeometry((json.dumps(a_geom))))
            except (ConnectionError,  HTTPError) as err:
                print('Error: '.format(err))
                #paramsConveted.append (value)

        return paramsConveted

    def response_resquest_with_attributes(self,  attributes_functions_name):
        a_dict ={}
        attributes = attributes_functions_name.strip().split(',')
        self.current_object = self.object_model
        for attr_name in attributes:
           obj = self._value_from_object(self.object_model, attr_name, [])

           if isinstance(obj, GEOSGeometry):
               geom = obj
               obj = json.loads(obj.geojson)
               if len(attributes) == 1:
                   return (obj, 'application/vnd.geo+json', geom)

           a_dict[attr_name] = obj

        return (a_dict, 'application/json')

    def response_request_attributes_functions_str_with_url(self, attributes_functions_str):
        attributes_functions_str = re.sub(r':/+', '://', attributes_functions_str)
        arr_of_two_url = self.attributes_functions_splitted_by_url(attributes_functions_str)
        resp = requests.get(arr_of_two_url[1])
        if resp.status_code == 404:
            return Response({'Erro:' + str(resp.status_code)}, status=status.HTTP_404_NOT_FOUND)
        j = resp.text
        attributes_functions_str = arr_of_two_url[0] + j

        output = self.response_of_request(attributes_functions_str)

    def response_of_request(self,  attributes_functions_str):
        att_funcs = attributes_functions_str.split('/')

        obj = self.get_geometry_object(self.object_model)

        if (not self.object_model.is_operation(att_funcs[0])) and self.object_model.is_attribute(att_funcs[0]):
            att_funcs = att_funcs[1:]

        self.current_object_state = self._execute_attribute_or_method(obj, att_funcs[0], att_funcs[1:])
        a_value = self.current_object_state
        if isinstance(a_value, GEOSGeometry):
            geom = a_value
            a_value = json.loads(a_value.geojson)
            return (a_value, 'application/vnd.geo+json', geom)
        elif isinstance(a_value, SpatialReference):
           a_value = { self.function_name(att_funcs): a_value.pretty_wkt }
        else:
            a_value = {
                self.function_name(att_funcs): a_value
            }

        return (a_value, 'application/json')

class FeatureResource(SpatialResource):

    def __init__(self):
        super(FeatureResource, self).__init__()
        feature_model = None

    def operations_with_parameters_type(self):

        dic = {}

        dic['area'] = []
        dic['boundary'] = []
        dic['buffer'] = [float]
        dic['centroid'] = []
        dic['contains'] = [GEOSGeometry]
        dic['convex_hull'] = []
        dic['coord_seq'] = []
        dic['coords'] = []
        dic['coord_seq'] = []
        dic['count'] = [float]
        dic['crosses'] = [GEOSGeometry]
        dic['crs'] = []
        dic['difference'] = [GEOSGeometry]
        dic['dims'] = []
        dic['disjoint'] = [GEOSGeometry]
        dic['distance'] = [GEOSGeometry]
        dic['empty'] = []
        dic['envelope'] = []
        dic['equals'] = [GEOSGeometry]
        dic['equals_exact'] = [GEOSGeometry]
        dic['ewkb'] = []
        dic['ewkt'] = []
        dic['extend'] = []
        dic['extent'] = [tuple]
        dic['geojson'] = []
        dic['geom_type'] = []
        dic['geom_typeid'] = []
        dic['get_coords'] = []
        dic['get_srid'] = []
        dic['get_x'] = []
        dic['get_y'] = []
        dic['get_z'] = []
        dic['has_cs'] = []
        dic['hasz'] = []
        dic['hex'] = []
        dic['hexewkb'] = []
        dic['index'] = []
        dic['intersection'] = [GEOSGeometry]
        dic['intersects'] = [GEOSGeometry]
        dic['json'] = []
        dic['kml'] = []
        dic['length'] = []
        dic['normalize'] = []
        dic['num_coords'] = []
        dic['num_geom'] = []
        dic['num_points'] = []
        dic['ogr'] = []
        dic['overlaps'] = [GEOSGeometry]
        dic['point_on_surface'] = []
        dic['pop'] = []
        dic['prepared'] = []
        dic['ptr'] = []
        dic['ptr_type'] = []
        dic['relate'] = [GEOSGeometry]
        dic['relate_pattern'] = [GEOSGeometry, str]
        dic['remove'] = [str]
        dic['reverse'] = []
        dic['ring'] = []
        dic['set_coords'] = [tuple]
        dic['set_srid'] = [int]
        dic['set_x'] = [float]
        dic['set_y'] = [float]
        dic['set_z'] = []
        dic['simple'] = []
        dic['simplify'] = [float, bool]
        dic['srid'] = []
        dic['srs'] = []
        dic['sym_difference'] = [GEOSGeometry]
        dic['touches'] = [GEOSGeometry]
        dic['transform'] = [int, bool]
        dic['tuple'] = []
        dic['union'] = [GEOSGeometry]
        dic['valid'] = []
        dic['valid_reason'] = [GEOSGeometry]
        dic['within'] = []
        dic['wkb'] = []
        dic['wkt'] = []
        dic['x'] = []
        dic['y'] = []
        dic['z'] = []
        return dic

    def set_model_status(self, a_const_status):
        self.model_status = a_const_status

    def basic_get(self, request, *args, **kwargs):

        self.object_model = self.get_object(kwargs)
        self.current_object_state = self.object_model
        self.set_context_resource(request)
        # self.request.query_params.
        attributes_functions_str = kwargs.get(self.attributes_functions_name_template())

        if attributes_functions_str is None:
            serializer = self.serializer_class(self.object_model)
            output = (serializer.data, 'application/vnd.geo+json', self.object_model)
            #self._set_context_to_model(object_model)

        elif self.has_only_attribute(attributes_functions_str):
            output = self.response_resquest_with_attributes(attributes_functions_str)
            dict_attribute = output[0]
            if len(attributes_functions_str.split(',')) > 1:
                self._set_context_to_attributes(dict_attribute.keys())
            else:
                self._set_context_to_object(attributes_functions_str)
        elif self.attributes_functions_str_has_url(attributes_functions_str.lower()):
            output = self.response_request_attributes_functions_str_with_url( attributes_functions_str)
            self._set_context_to_object(attributes_functions_str)
        else:
            output = self.response_of_request(attributes_functions_str)
            self._set_context_to_object(attributes_functions_str.split('/')[-1])

        return output

    def get(self, request, *args, **kwargs):

        dict_for_response = self.basic_get(request, *args, **kwargs)
        accept = request.META['HTTP_ACCEPT']
        if accept.lower() == "image/png" or kwargs.get('format', None) == 'png':
            if len(dict_for_response) == 3:
                queryset = dict_for_response[2]
                image = self.get_png(queryset, request)
                # headers = response._headers
                return HttpResponse(image, content_type="image/png")
                # headers.update(response._headers)
                # response._headers = headers
            else:
                return Response({'Erro': 'The server can generate an image only from a geometry data'},
                                status=status.HTTP_404_NOT_FOUND)

        return Response(data=dict_for_response[0], content_type=dict_for_response[1])

    def options(self, request, *args, **kwargs):
        self.basic_get(request, *args, **kwargs)
        #return self.context_resource.context()
        return Response ( data=self.context_resource.context(), content_type='application/json' )

class SpatialCollectionResource(AbstractResource):
    pass

class FeatureCollectionResource(SpatialCollectionResource):
    def get_queryset(self):
        stFunction = self.kwargs.get("attributes_functions", None)
        modelClass = self.serializer_class.Meta.model

        if stFunction is None:  # to get query parameters
            queryset = modelClass.objects.all()
            query_parameters = self.request.query_params
            dict = self.get_dict_with_spatialfunction_or_same_dict(query_parameters.dict())
            self.queryset = queryset.filter(**dict)

        else:  # to get query from url
            geom_str_or_url = self.kwargs.get('geom')
            aKey = self.serializer_class.Meta.geo_field + '__' + stFunction
            aGeom = self.geos_geometry(geom_str_or_url)

            if stFunction is not None:
                self.queryset = modelClass.objects.filter(**({aKey: aGeom}))

        return self.queryset

    def options(self, request, *args, **kwargs):
        pass