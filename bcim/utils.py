import json

import requests
from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
        return 'spatial_function'

    def spatial_function_parameter_template(self):
        return 'param'

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
                    a_geom = resp.json()["geometry"]
                    paramsConveted.append(GEOSGeometry((json.dumps(a_geom))))
            except ValueError:
                paramsConveted.append ( value)

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

    def dic_with_only_identitier_field(self):
        a_dict = {}
        for key, value in self.kwargs.items():
            if key != self.spatial_function_name_template() and key != self.spatial_function_parameter_template():
                a_dict[key] = value
                break
        return a_dict

    def get_geometry_object(self, object_model):
        return getattr(object_model, self.geometry_field_name(), None)


    def get(self, request, *args, **kwargs):

        object_model = self.get_object(self.dic_with_only_identitier_field())
        st_function = self.kwargs.get(self.spatial_function_name_template())
        if not st_function:
           serializer = self.serializer_class(object_model)
           res = Response(serializer.data)
           return res

        param = self.kwargs.get(self.spatial_function_parameter_template())
        if param:
            params = self.parametersConverted(param)
            obj_geometry = self.get_geometry_object(object_model)
            res = getattr(obj_geometry , st_function)(*params)
        else:
            res = getattr(self.get_geometry_object(object_model), st_function)

        if isinstance(res, GEOSGeometry):
            return JSONResponse(res.geojson)

        a_dict = {st_function : res}
        return Response(a_dict)
