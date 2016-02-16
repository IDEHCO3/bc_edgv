import json

import requests
from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from requests.packages.urllib3.exceptions import HTTPError, ConnectionError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(data, **kwargs)

class DefaultsMixin(object):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    paginate_by = 250

    # Default settings for view authentication, permissions, filtering and pagination.
"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
"""

import ast
from django.contrib.gis.geos import GeometryCollection, GEOSGeometry

class ResourceListCreateFilteredByQueryParameters(generics.ListCreateAPIView):

    def get_queryset(self):
        model_class = self.serializer_class.Meta.model
        queryset = model_class.objects.all()
        query_parameters = self.request.query_params
        dict = self.get_dict_with_spatialfunction_or_same_dict(query_parameters.dict())

        queryset = queryset.filter(**dict)
        return queryset

    def get_dict_with_spatialfunction_or_same_dict(self, dict):
        for key, value in dict.items():
            if key.startswith('*'):
                new_key = self.serializer_class.Meta.geo_field + '__' + key[1:]
                dict.pop(key)
                #a_value = value
                #a_geom = GEOSGeometry(a_value, 4326)
                dict[new_key] = value
        return dict



class BasicListFiltered(generics.ListCreateAPIView):

    def get_queryset(self):

        st_function = self.kwargs.get("spatial_function")
        geom_str_or_url = self.kwargs.get('geom')
        url_rest = self.request.query_params.get('url', None)
        a_key = self.serializer_class.Meta.geo_field + '__' + st_function
        aGeom = self.geos_geometry(geom_str_or_url)

        if st_function is not None:
            model_class = self.serializer_class.Meta.model
            return model_class.objects.filter(**({a_key: aGeom}))

        return self.queryset

    def make_geometrycollection_from_featurecollection(feature_collection):
        geoms = []
        features = ast.literal_eval(feature_collection)
        for feature in features['features']:
            feature_geom = feature['geometry']
            geoms.append(GEOSGeometry(feature_geom))
        return GeometryCollection(tuple(geoms))


    def geos_geometry(self, geom_str_or_url):
        a_geom =  geom_str_or_url
        str1 = (geom_str_or_url[0:5]).lower()
        https = ['http:', 'https']
        if (str1 in https):
            resp= requests.get(geom_str_or_url)
            j = resp.json()
            if j["type"].lower()== 'feature':
               return GEOSGeometry(json.dumps(j["geometry"]))
            return self.make_geometrycollection_from_featurecollection(resp.text)
        return GEOSGeometry(a_geom)


class APIViewBasicSpatialFunction(APIView):

    def model_class(self):
        return self.serializer_class.Meta.model

    def geometry_field_name(self):
        return self.serializer_class.Meta.geo_field

    def spatial_function_name_template(self):
        return 'spatial_function_'

    def function_name_template(self):
        return 'function_'

    def spatial_function_parameter_template(self):
        return 'param_'

    def key_is_spatial_function(self, a_key):
        return a_key[0:17] ==  self.spatial_function_name_template() # len of spatial_function_

    def key_is_not_spatial_function(self, a_key):
        return not self.key_is_spatial_function(a_key)

    def key_is_function(self, a_key):
        return a_key[0:9] ==  self.function_name_template() # len of function_

    def key_is_not_function(self, a_key):
        return not self.key_is_function( a_key)

    def key_is_param(self, a_key):
        return a_key[0:6] ==  self.spatial_function_parameter_template() # len of param_

    def key_is_not_param(self, a_key):
        return not self.key_is_param(a_key)

    def key_is_identifier(self, a_key):
        return self.key_is_not_spatial_function(a_key) and self.key_is_not_param(a_key) and self.key_is_not_function(a_key)


    def dic_with_only_identitier_field(self, dict_params):
        dic = dict_params.copy()
        a_dict = {}
        for key, value in dic.items():
            if self.key_is_identifier(key):
                a_dict[key] = value
        return a_dict

    def parametersConverted(self, params_as_ampersand_string):
        paramsConveted = []
        params_as_array = params_as_ampersand_string.split('&')
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

class APIViewDetailSpatialFunction(APIViewBasicSpatialFunction):
    """
    Retrieve, update or delete a object instance.
    """

    def get_object(self, a_dict):
        queryset = self.model_class().objects.all()
        obj = get_object_or_404(queryset, **a_dict)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_geometry_object(self, object_model):
        return getattr(object_model, self.geometry_field_name(), None)

    def spatial_functions_with_params(self, dict_params):
        a_dic_sf_param = {}
        for i in range(len(dict_params)):
           sf = dict_params.get('spatial_function_' + str(i+1))
           if sf is not None:
              a_dic_sf_param[sf] = dict_params.get('param_' + str(i+1))
        return a_dic_sf_param

    def get(self, request, *args, **kwargs):
        object_model = self.get_object(self.dic_with_only_identitier_field(kwargs))

        st_functions = self.spatial_functions_with_params(kwargs)

        if len(st_functions) == 0:
           serializer = self.serializer_class(object_model)
           res = Response(serializer.data)
           return res

        obj_geometry = self.get_geometry_object(object_model)
        for st_name, param_value in st_functions.items():
            if param_value:
                params = self.parametersConverted(param_value)
                obj_geometry = getattr(obj_geometry, st_name)(*params)
            else:
                obj_geometry = getattr(obj_geometry, st_name)

        if isinstance(obj_geometry, GEOSGeometry):
          return JSONResponse(obj_geometry.geojson)

        a_dict = { st_functions.__str__(): obj_geometry}
        return Response(a_dict)
