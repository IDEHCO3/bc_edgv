from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry, Point, Polygon, MultiPolygon,LineString, MultiLineString, MultiPoint, GeometryCollection
from datetime import date, datetime
from time import *

from django.db.models import *


def vocabularyDict():

    dic = {}
    dic[BooleanField] = 'http://schema.org/Boolean'
    dic[bool] = 'http://schema.org/Boolean'
    dic[FloatField] = 'http://schema.org/Float'
    dic[float] = 'http://schema.org/Float'
    dic[IntegerField] = 'http://schema.org/Integer'
    dic[int] = 'http://schema.org/Integer'
    dic[CharField] = 'http://schema.org/Text'
    dic[str] = 'http://schema.org/Text'
    dic[DateField] = 'http://schema.org/Date'
    dic[date] = 'http://schema.org/Date'
    dic[DateTimeField] = 'http://schema.org/DateTime'
    dic[datetime] = 'http://schema.org/DateTime'
    dic[TimeField] = 'http://schema.org/Time'
    dic[Model] = 'http://geojson.org/geojson-ld/vocab.html#Feature'
    dic['FeatureCollection'] = 'http://geojson.org/geojson-ld/vocab.html#FeatureCollection'
    dic['GeometryField'] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic[GEOSGeometry] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic['PointField'] = 'http://geojson.org/geojson-ld/vocab.html#Point'
    dic[Point] = 'http://geojson.org/geojson-ld/vocab.html#Point'
    dic['LineStringField'] = 'http://geojson.org/geojson-ld/vocab.html#LineString'
    dic[LineString] = 'http://geojson.org/geojson-ld/vocab.html#LineString'
    dic['PolygonField'] = 'http://geojson.org/geojson-ld/vocab.html#Polygon'
    dic[Polygon] = 'http://geojson.org/geojson-ld/vocab.html#Polygon'
    dic['MultiPolygonField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiPolygon'
    dic[MultiPolygon] = 'http://geojson.org/geojson-ld/vocab.html#MultiPolygon'
    dic['MultiLineStringField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiLineString'
    dic[MultiLineString] = 'http://geojson.org/geojson-ld/vocab.html#MultiLineString'
    dic['MultiPointField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiPoint'
    dic[MultiPoint] = 'http://geojson.org/geojson-ld/vocab.html#MultiPoint'
    dic['GeometryCollection'] = 'http://geojson.org/geojson-ld/vocab.html#GeometryCollection'
    dic[GeometryCollection] = 'http://geojson.org/geojson-ld/vocab.html#GeometryCollection'

    dic['nome'] = 'http://schema.org/name'
    dic['nomeAbrev'] = 'https://schema.org/alternateName'

    return dic

class Reflection:

    def superclass(a_class):
        return a_class.__base__

    def supeclasses(a_class):
        return a_class.__bases__

    def operation_names(a_class):
        return [method for method in dir ( a_class ) if
                callable ( getattr ( a_class, method ) ) and a_class.is_not_private ( method )]

class ContextResource:

    def __init__(self):
        self.basic_path = None
        self.host = None
        self.dict_context = None


    #def attribute_name_list(self):
    #    return ( field.attname for field in self.model_class._meta.fields[:])

    #def attribute_type_list(self):
    #    return ( type(field) for field in self.model_class._meta.fields[:])

    def operation_names(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and self.is_not_private(method)]

    def attributeContextualized_dict(self, att='', writeable=True, readable=True, required=False):
        dic = {}
        dic["property"] = att
        dic["writeable"] = writeable
        dic["readable"] = readable
        dic["required"] = required
        return dic

    def selectedAttributeContextualized_dict(self, attribute_name_array):

        return {k: v for k, v in self.attributeContextualized_dict().iteritems() if k in attribute_name_array}

    def hydraSuportedProperties(self):
        arr = [];
        for  field in self.model_class._meta.fields:
            arr.append(self.hydraSuportedProperty(field.attname, True, True, False))
        return arr;

    def generateSuportedProperties(self):
        dic = {}
        dic["suportedProperty"] = self.hydraSuportedProperties()
        return dic

    def attributeContextualized(self, aFieldFromModel):
       pass

    def attributeContextualized_list(self):
        dic_context = {}
        return dic_context

    def supportedProperties(self):
        arr_dic = [ ]
        return {arr_dic }

    def supportedOperations(self):
        arr_dic = [
            {"hydra:method": "GET","hydra:operation": "srs","hydra:expects":"", "hydra:returns": "",  "hydra:statusCode": ""},
            {"hydra:method": "GET","hydra:operation": "envelope","hydra:expects":"", "hydra:returns": "http://geojson.org/geojson-ld/vocab.html#geometry",  "hydra:statusCode": ""},
        ]
        return arr_dic

    def iriTemplates(self):
        return {}

    def set_context_to_attributes(self, attributes_name):
        self.dict_context = {}
        self.dict_context["@context"] = self.selectedAttributeContextualized_dict(attributes_name)

    def set_context_to_object(self, object, attribute_name, parameters, returned_value_type):
        self.dict_context = {}
        self.dict_context["@context"] = self.selectedAttributeContextualized_dict([attribute_name])

        isGeometry = isinstance(getattr(object, attribute_name, None), GEOSGeometry)
        if isGeometry:
           self.dict_context["hydra:supportedOperations"] = self.supportedOperations()

    def initalize_context(self):
        self.dict_context = {}
        self.dict_context["@context"] = self.attributeContextualized_dict()
        self.dict_context["hydra:supportedProperty"] = self.supportedProperties()
        self.dict_context["hydra:supportedOperations"] = self.supportedOperations()
        self.dict_context["hydra:iriTemplate"] = self.iriTemplates()

        return self.dict_context

    def context(self):
        if self.dict_context is None:
            self.initalize_context()
        return self.dict_context

    def set_context_(self, dictionary):
        self.dict_context = dictionary

class FeatureContext(ContextResource):

    def supportedProperties(self):
        arr_dic = [ ]
        return {arr_dic }

    def supportedOperations(self):


        arr_dic = [
            {"hydra:method": "GET","hydra:operation": "srs","hydra:expects":"", "hydra:returns": "",  "hydra:statusCode": ""},
            {"hydra:method": "GET","hydra:operation": "envelope","hydra:expects":"", "hydra:returns": "http://geojson.org/geojson-ld/vocab.html#geometry",  "hydra:statusCode": ""},
        ]
        return arr_dic

    def iriTemplates(self):
        return {}