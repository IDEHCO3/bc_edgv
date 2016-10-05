import json

import requests
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import six
from requests.exceptions import HTTPError, ConnectionError
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework.compat import (
    INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS
)

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

    # paginate_by = 250
    #
    # Default settings for view authentication, permissions, filtering and pagination.

    # authentication_classes = (
    #     authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    # )

import ast
from django.contrib.gis.geos import GeometryCollection, GEOSGeometry

class Type_Called():
    def __init__(self, a_name, params, answer):
        self.name = a_name
        self.parameters = params
        self.return_type = answer

class FeatureModel(models.Model):

    def __init__(self, a_hyperlink):
        self.hyperlink = a_hyperlink
        self.dic = {}

    def centroid(self):
       return self.geom.centroid

    def ring(self):
        return self.geom.ring

    def crs(self):
        return self.geom.crs

    def wkt(self):
        return self.geom.wkt

    def srs(self):
        return self.geom.srs

    def hexewkb(self):
        return self.geom.hexewkb

    def equals_exact(self, other_GEOSGeometry, tolerance=0):
        return self.geom.equals_exact(other_GEOSGeometry, tolerance)

    def set_srid(self, a_srid):
        return self.geom.set_srid(a_srid)

    def hex(self):
        return self.geom.hex

    def has_cs(self):
        return self.geom.has_cs

    def area(self):
        return self.geom.area

    def extend(self):
        return self.geom.extend

    def wkb(self):
        return self.geom.wkb

    def geojson(self):
        return self.geom.geojson

    def relate(self, other_GEOSGeometry, pattern):
        return self.geom.relate(other_GEOSGeometry, pattern)

    def set_coords(self, coords):
        return self.geom.set_coords(coords)

    def simple(self):
        return self.geom.simple

    def geom_type(self):
        return self.geom.geom_type

    def set_y(self, y):
        return self.geom.set_y(y)

    def normalize(self):
        return self.geom.normalize

    def sym_difference(self, other_GEOSGeometry):
        return self.geom.sym_difference(other_GEOSGeometry)

    def valid_reason(self):
        return self.geom.valid_reason

    def geom_typeid(self):
        return self.geom.geom_typeid

    def valid(self):
        return self.geom.valid

    def ogr(self):
        return self.geom.ogr

    def coords(self):
        return self.geom.coords

    def num_coords(self):
        return self.geom.num_coords

    def get_srid(self):
        return self.geom.get_srid

    def distance(self, other_GEOSGeometry):
        return self.geom.distance(other_GEOSGeometry)

    def json(self):
        return self.geom.json

    def pop(self):
        return self.geom.pop

    def ewkb(self):
        return self.geom.ewkb

    def x(self):
        return self.geom.x

    def simplify(self, tolerance=0.0, preserve_topology=False):
        return self.geom.simplify(tolerance=0.0, preserve_topology=False)

    def set_z(self):
        return self.geom.set_z

    def buffer(self, width, quadsegs=8):
        return self.geom.buffer(width, quadsegs)

    def relate_pattern(self, other_GEOSGeometry, pattern):
        return self.geom.relate_pattern(other_GEOSGeometry, pattern)

    def z(self):
        return self.geom.z

    def num_geom(self):
        return self.geom.num_geom

    def coord_seq(self):
        return self.geom.coord_seq

    def dims(self):
        return self.geom.dims

    def get_y(self):
        return self.geom.get_y

    def tuple(self):
        return self.geom.tuple

    def y(self):
        return self.geom.y

    def convex_hull(self):
        return self.geom.convex_hull

    def get_x(self):
        return self.geom.get_x

    def index(self):
        return self.geom.index

    def boundary(self):
        return self.geom.boundary

    def kml(self):
        return self.geom.kml

    def touches(self, other_GEOSGeometry):
        return self.geom.touches(other_GEOSGeometry)

    def empty(self):
        return self.geom.empty

    def srid(self):
        return self.geom.srid

    def get_z(self):
        return self.geom.get_z

    def extent(self):
        return self.geom.extent

    def union(self, other_GEOSGeometry):
        return self.geom.union(other_GEOSGeometry)

    def intersects(self, other_GEOSGeometry):
        return self.geom.intersect(other_GEOSGeometry)

    def contains(self, other_GEOSGeometry):
        return self.geom.contains(other_GEOSGeometry)

    def hasz(self):
        return self.geom.hasz

    def crosses(self, other_GEOSGeometry):
        return self.geom.crosses(other_GEOSGeometry)

    def count(self):
        return self.geom.count

    def num_points(self):
        return self.geom.num_points

    def within(self, other_GEOSGeometry):
        return self.geom.within(other_GEOSGeometry)

    def intersection(self, other_GEOSGeometry):
        return self.geom.intersection(other_GEOSGeometry)

    def overlaps(self, other_GEOSGeometry):
        return self.geom.overlaps(other_GEOSGeometry)

    def equals(self, other_GeosGeometry ):
        return self.geom.equals( other_GeosGeometry)

    def point_on_surface(self):
        return self.geom.point_on_surface

    def difference(self, other_GEOSGeometry):
        return self.geom.difference(other_GEOSGeometry)

    def transform(self,srid, clone=True ):
        return self.geom.transform(srid, clone=True)

    def set_x(self, x):
        return self.geom.set_x(x)

    def get_coords(self):
        return self.geom.get_coords

    def envelope(self):
        return self.geom.envelope

    def prepared(self):
        return self.geom.prepared

    def ewkt(self):
        return self.geom.ewkt

    def length(self):
        return self.geom.length

    def disjoint(self, other_GEOSGeometry):
        return self.geom.disjoint(other_GEOSGeometry)

    def geometry_with_parameters_type(self):
        #self.dic = [   '', '', 'intersects', 'json', 'kml', 'length', 'normalize', 'num_coords', 'num_geom', 'num_points', 'ogr', 'overlaps', 'point_on_surface', 'pop', 'prepared', 'ptr', 'ptr_type', 'relate', 'relate_pattern', 'remove', 'reverse', 'ring', 'set_coords', 'set_srid', 'set_x', 'set_y', 'set_z', 'simple', 'simplify', 'sort', 'srid', 'srs', 'sym_difference', 'touches', 'transform', 'tuple', 'union', 'valid', 'valid_reason', 'within', 'wkb', 'wkt', 'x', 'y', 'z']

        if len(self.dic) == 0:
            self.dic['area'] = Type_Called('area', None, float)
            self.dic['boundary'] = Type_Called('boundary', None, float)
            self.dic['buffer'] = Type_Called('buffer', [float], GEOSGeometry)
            self.dic['centroid'] = Type_Called('centroid', None, Point)
            self.dic['contains'] = Type_Called('contains', [GEOSGeometry], bool)
            self.dic['convex_hull'] = Type_Called('convex_hull', None, Polygon)
            self.dic['coord_seq'] = Type_Called('coord_seq', None, tuple)
            self.dic['coords'] = Type_Called('coords', None, tuple)
            self.dic['count'] = Type_Called('count', None, int)
            self.dic['crosses'] = Type_Called('crosses', [GEOSGeometry], bool)
            self.dic['crs'] = Type_Called('crs', None, SpatialReference)
            self.dic['difference'] = Type_Called('difference', [GEOSGeometry], GEOSGeometry)
            self.dic['dims'] = Type_Called('dims', None, int)
            self.dic['disjoint'] = Type_Called('disjoint',[GEOSGeometry], bool)
            self.dic['distance'] = Type_Called('distance',[GEOSGeometry], float)
            self.dic['empty'] = Type_Called('empty',None, bool)
            self.dic['envelope'] = Type_Called('envelope',None, GEOSGeometry)
            self.dic['equals'] = Type_Called('equals',[GEOSGeometry], bool)
            self.dic['equals_exact'] = Type_Called('equals_exact',[GEOSGeometry, float], bool)
            self.dic['ewkb'] = Type_Called('ewkb',None, str)
            self.dic['ewkt'] = Type_Called('ewkt',None, str)
            self.dic['extend'] = Type_Called('extend',None, tuple)
            self.dic['extent'] = Type_Called('extent',None, tuple)
            self.dic['geojson'] = Type_Called('geojson',None, str)
            self.dic['geom_type'] = Type_Called('geom_type',None, str)
            self.dic['geom_typeid'] = Type_Called('geom_typeid',None, int)
            self.dic['get_coords'] = Type_Called('get_coords', None, tuple)
            self.dic['get_srid'] = Type_Called('get_srid', None, str)
            self.dic['get_x'] = Type_Called('get_x', None, str)
            self.dic['get_y'] = Type_Called('get_y', None, str)
            self.dic['get_z'] = Type_Called('get_z', None, str)
            self.dic['has_cs'] = Type_Called('has_cs',None, bool)
            self.dic['hasz'] = Type_Called('hasz',None, bool)
            self.dic['hex'] = Type_Called('hex',None, str)
            self.dic['hexewkb'] = Type_Called('hexewkb',None, str)
            self.dic['index'] = Type_Called('index',None, int)
            self.dic['intersection'] = Type_Called('intersection',[GEOSGeometry], GEOSGeometry)
            self.dic['intersects'] = Type_Called('intersects',[GEOSGeometry], bool)
            self.dic['interpolate'] = Type_Called('interpolate',[float], Point)
            self.dic['json'] = Type_Called('json',None, str)
            self.dic['kml'] = Type_Called('kml',None, str)
            self.dic['length'] = Type_Called('length',None, float)
            self.dic['normalize'] = Type_Called('normalize',[float], Point)
            self.dic['num_coords'] = Type_Called('num_coords',None, int)
            self.dic['num_geom'] = Type_Called('num_geom',None, int)
            self.dic['num_points'] = Type_Called('num_points',None, int)
            self.dic['ogr'] = Type_Called('ogr',None,  OGRGeometry)
            self.dic['overlaps'] = Type_Called('overlaps',[GEOSGeometry],  bool)
            self.dic['point_on_surface'] = Type_Called('point_on_surface',None,  Point)
            self.dic['pop'] = Type_Called('pop',None,  tuple)
            self.dic['prepared'] = Type_Called('prepared',None,  PreparedGeometry)
            self.dic['relate'] = Type_Called('relate',[GEOSGeometry],  str)
            self.dic['relate_pattern'] = Type_Called('relate_pattern',[GEOSGeometry, str],  str)
            self.dic['ring'] = Type_Called('ring',None,  bool)
            self.dic['set_coords'] = Type_Called('set_coords',[tuple],  None)
            self.dic['set_srid'] = Type_Called('set_srid',[str],  None)
            self.dic['set_x'] = Type_Called('set_x',[float],  None)
            self.dic['set_y'] = Type_Called('set_y',[float],  None)
            self.dic['set_z'] = Type_Called('set_z',[float],  None)
            self.dic['simple'] = Type_Called('simple',None,  bool)
            self.dic['simplify'] = Type_Called('simplify', [float, bool],  GEOSGeometry)
            self.dic['srid'] = Type_Called('srid', None,  int)
            self.dic['srs'] = Type_Called('srs', None,  SpatialReference)
            self.dic['sym_difference'] = Type_Called('sym_difference', [GEOSGeometry],  GEOSGeometry)
            self.dic['touches'] = Type_Called('touches', [GEOSGeometry],  bool)
            self.dic['transform'] = Type_Called('transform', [int, bool],  GEOSGeometry)
            self.dic['tuple'] = Type_Called('tuple', None,  tuple)
            self.dic['union'] = Type_Called('union', [GEOSGeometry],  GEOSGeometry)
            self.dic['valid'] = Type_Called('valid', [GEOSGeometry],  bool)
            self.dic['valid_reason'] = Type_Called('valid_reason', [GEOSGeometry],  str)
            self.dic['within'] = Type_Called('within', [GEOSGeometry],  bool)
            self.dic['wkb'] = Type_Called('wkb', None,  str)
            self.dic['wkt'] = Type_Called('wkt', None,  str)
            self.dic['x'] = Type_Called('x', None,  float)
            self.dic['y'] = Type_Called('y', None,  float)
            self.dic['z'] = Type_Called('z', None,  float)
        return self.dic

def geometry_with_parameters_type():

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

class ResourceListCreateFilteredByQueryParameters(generics.ListCreateAPIView):

    def get_queryset(self):
        model_class = self.serializer_class.Meta.model
        queryset = model_class.objects.all()
        query_parameters = self.request.query_params
        dict = self.get_dict_with_spatialfunction_or_same_dict(query_parameters.dict())

        queryset = queryset.filter(**dict)
        return queryset

    def json_geometrycollection_from_featurecollection(self, feature_collection):
        geometry_collection = {
            "type": "GeometryCollection",
            "geometries": []
        }

        for feature in feature_collection['features']:
            geometry_collection['geometries'].append(feature['geometry'])

        return json.dumps(geometry_collection)

    def make_geometrycollection_from_featurecollection(self, feature_collection):
        geoms = []
        features = ast.literal_eval(feature_collection)
        for feature in features['features']:
            feature_geom = feature['geometry']
            geoms.append(GEOSGeometry(feature_geom))
        return GeometryCollection(tuple(geoms))

    def get_dict_with_spatialfunction_or_same_dict(self, dict):
        for key, value in dict.items():
            if key.startswith('*'):
                new_key = self.serializer_class.Meta.geo_field + '__' + key[1:]
                dict.pop(key)
                str1 = (value[0:5]).lower()
                https = ['http:', 'https']
                if (str1 in https):
                    resp = requests.get(value)
                    j = resp.json()

                    if j["type"].lower() == 'feature':
                        value = json.dumps(j["geometry"])
                    elif j["type"].lower() == 'featurecollection':
                        value = self.json_geometrycollection_from_featurecollection(resp.json())
                    else:
                        value = json.dumps(j)

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

    def make_geometrycollection_from_featurecollection(self, feature_collection):
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

            if j["type"].lower() == 'feature':
               return GEOSGeometry(json.dumps(j["geometry"]))

            if j["type"].lower() == 'featurecollection':
                return self.make_geometrycollection_from_featurecollection(resp.text)

            a_geom = json.dumps(j)

        return GEOSGeometry(a_geom)


class BasicAPIViewHypermedia(APIView):

    def model_class(self):
        return self.serializer_class.Meta.model

    def geometry_field_name(self):
        return self.serializer_class.Meta.geo_field

    def get_geometry_object(self, object_model):
        return getattr(object_model, self.geometry_field_name(), None)

    def key_is_identifier(self, key):
        return key in self.serializer_class.Meta.identifiers

    def dic_with_only_identitier_field(self, dict_params):
        dic = dict_params.copy()
        a_dict = {}
        for key, value in dic.items():
            if self.key_is_identifier(key):
                a_dict[key] = value

        return a_dict

    def is_spatial_operation(self, attribute_or_method_name):
        return (attribute_or_method_name in geometry_with_parameters_type().keys())

    def is_spatial_attribute(self, attribute_or_method_name):
        return self.geometry_field_name() == attribute_or_method_name

    def is_spatial_and_has_parameters(self, attribute_or_method_name):
        dic = geometry_with_parameters_type()
        return (attribute_or_method_name in dic) and len(dic[attribute_or_method_name])

class APIViewHypermedia(BasicAPIViewHypermedia):


    def get_object(self, a_dict):
        queryset = self.model_class().objects.all()
        obj = get_object_or_404(queryset, **a_dict)
        self.check_object_permissions(self.request, obj)
        return obj

    def attributes_functions_name_template(self):
        return 'attributes_functions'

    def _has_method(self, object, method_name):
        return hasattr(object, method_name) and callable(getattr(object, method_name))

    def has_only_attribute(self, object, attributes_functions_name):
        attrs_functs = attributes_functions_name.split('/')
        if len(attrs_functs) > 1:
            return False
        if '&' in attrs_functs[0]:
            return True

        if self._has_method(object, attrs_functs[0]):
            return False
        return hasattr(object, attrs_functs[0])


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

    def all_parameters_converted(self, attribute_or_function_name, parameters):
        parameters_converted = []
        if self.is_spatial_and_has_parameters(attribute_or_function_name):
            parameters_type = geometry_with_parameters_type()[attribute_or_function_name]
            for i in range(0, len(parameters)):
                parameters_converted.append(parameters_type[i](parameters[i]))
            return parameters_converted

        return self.parametersConverted(parameters)

    def _value_from_object(self, object, attribute_or_function_name, parameters):

        if len(parameters):
            params = self.all_parameters_converted(attribute_or_function_name, parameters)
            return getattr(object, attribute_or_function_name)(*params)

        return getattr(object, attribute_or_function_name)

    def response_resquest_with_attributes(self, object_model, attributes_functions_name):
        a_dict ={}
        attributes = attributes_functions_name.split('&')
        for attr_name in attributes:
           obj = self._value_from_object(object_model, attr_name, [])
           if isinstance(obj, GEOSGeometry):
                obj = json.loads( obj.geojson)
                if len(attributes) == 1:
                    return Response(obj,  content_type='application/vnd.geo+json')

           a_dict[attr_name] = obj

        return Response(a_dict, content_type='application/json')

    def attributes_functions_str_has_url(self, attributes_functions_str_url):
        return (attributes_functions_str_url.find('http:') > -1) or (attributes_functions_str_url.find('https:') > -1)\
               or (attributes_functions_str_url.find('www.') > -1)

    def attributes_functions_splitted_by_url(self, attributes_functions_str_url):
        res = attributes_functions_str_url.lower().find('http:')
        if res == -1:
            res = attributes_functions_str_url.lower().find('https:')
            if res == -1:
                res = attributes_functions_str_url.lower().find('www.')
                if res == -1:
                    return [attributes_functions_str_url]

        return [attributes_functions_str_url[0:res], attributes_functions_str_url[res:]]

    def _execute_attribute_or_method(self, object, attribute_or_method_name, array_of_attribute_or_method_name):
        dic = {}
        parameters = []
        arr_attrib_method_name = array_of_attribute_or_method_name
        att_or_method_name = attribute_or_method_name

        if self.is_spatial_and_has_parameters(att_or_method_name):
            parameters = arr_attrib_method_name[0].split('&')
            arr_attrib_method_name = arr_attrib_method_name[1:]

        obj = self._value_from_object(object, att_or_method_name, parameters)

        if len(arr_attrib_method_name) == 0:
            return obj

        return self._execute_attribute_or_method(obj, arr_attrib_method_name[0], arr_attrib_method_name[1:])

    def response_of_request(self, object, attributes_functions_str):
        att_funcs = attributes_functions_str.split('/')

        obj = self.get_geometry_object(object)
        if not self.is_spatial_operation ( att_funcs[0]) and self.is_spatial_attribute(att_funcs[0]):
            att_funcs = att_funcs[1:]

        a_value = self._execute_attribute_or_method(obj, att_funcs[0], att_funcs[1:] )

        if isinstance(a_value, GEOSGeometry):
           a_value =  json.loads( a_value.geojson)
           return Response(data=a_value, content_type='application/vnd.geo+json')

        return Response(data=a_value, content_type='application/json')

    def get(self, request, *args, **kwargs):
        object_model = self.get_object(self.dic_with_only_identitier_field(kwargs))

        attributes_functions_str = kwargs.get(self.attributes_functions_name_template())

        if attributes_functions_str is None:
            serializer = self.serializer_class(object_model)
            return Response(serializer.data,  content_type='application/vnd.geo+json')

        if self.has_only_attribute(object_model, attributes_functions_str):
            return self.response_resquest_with_attributes(object_model, attributes_functions_str )

        if self.attributes_functions_str_has_url(attributes_functions_str.lower()):
            arr_of_two_url = self.attributes_functions_splitted_by_url(attributes_functions_str)
            resp = requests.get(arr_of_two_url[1])
            if resp .status_code == 404:
                return Response({'Erro:' + str(resp.status_code)})
            j = resp.text
            attributes_functions_str = arr_of_two_url[0] + j

        return self.response_of_request(object_model, attributes_functions_str)


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

        a_dict = {st_functions.__str__(): obj_geometry}
        return Response(a_dict)
