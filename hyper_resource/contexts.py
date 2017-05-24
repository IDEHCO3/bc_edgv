from django.contrib.gis.db import models

def vocabularyDict():

    dic = {}
    dic['BooleanField'] = 'http://schema.org/Boolean'
    dic['FloatField'] = 'http://schema.org/Float'
    dic['IntegerField'] = 'http://schema.org/Integer'
    dic['CharField'] = 'http://schema.org/Text'
    dic['DateField'] = 'http://schema.org/Date'
    dic['DateTimeField'] = 'http://schema.org/DateTime'
    dic['TimeField'] = 'http://schema.org/Time'
    dic['Model'] = 'http://geojson.org/geojson-ld/vocab.html#Feature'
    dic['FeatureCollection'] = 'http://geojson.org/geojson-ld/vocab.html#FeatureCollection'
    dic['GeometryField'] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic['PointField'] = 'http://geojson.org/geojson-ld/vocab.html#Point'
    dic['LineStringField'] = 'http://geojson.org/geojson-ld/vocab.html#LineString'
    dic['PolygonField'] = 'http://geojson.org/geojson-ld/vocab.html#Polygon'
    dic['MultiPolygonField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiPolygon'
    dic['MultiLineStringField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiLineString'
    dic['MultiPointField'] = 'http://geojson.org/geojson-ld/vocab.html#MultiPoint'
    dic['GeometryCollection'] = 'http://geojson.org/geojson-ld/vocab.html#GeometryCollection'

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


    def attribute_name_list(self):
        return ( field.attname for field in self.model_class._meta.fields[:])

    def attribute_type_list(self):
        return ( type(field) for field in self.model_class._meta.fields[:])

    def operation_names(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and self.is_not_private(method)]

    def hydraSuportedProperty(self, att='', writeable=True, readable=True, required=False):
        dic = {}
        dic["property"] = att
        dic["writeable"] = writeable
        dic["readable"] = readable
        dic["required"] = required
        return dic

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

    def context(self):
        dic = {}
        #dic['@context'] = self.generateBaseContext()
        #dic['supportedProperties'] = self.generateSuportedProperties()
        return dic