from django.contrib.gis.db import models
from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models import LineStringField
from django.contrib.gis.db.models import MultiLineStringField
from django.contrib.gis.db.models import MultiPointField
from django.contrib.gis.db.models import MultiPolygonField
from django.contrib.gis.db.models import PointField
from django.contrib.gis.db.models import PolygonField
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.gdal import SpatialReference
from django.contrib.gis.geos import GEOSGeometry, Point, Polygon, MultiPolygon,LineString, MultiLineString, MultiPoint, GeometryCollection
from datetime import date, datetime
from time import *

from django.contrib.gis.geos.prepared import PreparedGeometry
from django.db.models import *


class Reflection:

    def superclass(a_class):
        return a_class.__base__

    def supeclasses(a_class):
        return a_class.__bases__

    def operation_names(a_class):
        return [method for method in dir ( a_class ) if
                callable ( getattr ( a_class, method ) ) and a_class.is_not_private ( method )]


class FeatureCollection(object):
    pass


def vocabularyDict():

    dic = {}

    dic[BooleanField] = 'http://schema.org/Boolean'
    dic[bool] = 'http://schema.org/Boolean'
    dic[True] = 'http://schema.org/Boolean'
    dic[False] = 'http://schema.org/Boolean'
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
    dic[tuple]= 'http://schema.org/ListItem'

    dic['nome'] = 'http://schema.org/name'
    dic['nomeAbrev'] = 'https://schema.org/alternateName'

    dic['FeatureCollection'] = 'http://geojson.org/geojson-ld/vocab.html#FeatureCollection'
    dic[GeometryField] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic[PointField] = 'http://geojson.org/geojson-ld/vocab.html#Point'
    dic[LineStringField] = 'http://geojson.org/geojson-ld/vocab.html#LineString'
    dic[PolygonField] = 'http://geojson.org/geojson-ld/vocab.html#Polygon'
    dic[MultiPolygonField] = 'http://geojson.org/geojson-ld/vocab.html#MultiPolygon'
    dic[MultiLineStringField] = 'http://geojson.org/geojson-ld/vocab.html#MultiLineString'
    dic[MultiPointField] = 'http://geojson.org/geojson-ld/vocab.html#MultiPoint'

    dic[MultiPolygon] = 'http://geojson.org/geojson-ld/vocab.html#MultiPolygon'
    dic[Polygon] = 'http://geojson.org/geojson-ld/vocab.html#Polygon'
    dic[LineString] = 'http://geojson.org/geojson-ld/vocab.html#LineString'
    dic[Point] = 'http://geojson.org/geojson-ld/vocab.html#Point'
    dic[GEOSGeometry] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic[OGRGeometry] = 'http://geojson.org/geojson-ld/vocab.html#geometry'
    dic[MultiLineString] = 'http://geojson.org/geojson-ld/vocab.html#MultiLineString'
    dic[MultiPoint] = 'http://geojson.org/geojson-ld/vocab.html#MultiPoint'
    dic[GeometryCollection] = 'http://geojson.org/geojson-ld/vocab.html#GeometryCollection'
    dic[SpatialReference] = 'http://geojson.org/geojson-ld/vocab.html#SpatialReference'


    dic['area'] = 'http://opengis.org/operations/area'
    dic['boundary'] = 'http://opengis.org/operations/boundary'
    dic['buffer'] = 'http://opengis.org/operations/buffer'
    dic['centroid'] = 'http://opengis.org/operations/centroid'
    dic['contains'] = 'http://opengis.org/operations/contains'
    dic['convex_hull'] = 'http://opengis.org/operations/convex_hull'
    dic['coord_seq'] = 'http://opengis.org/operations/coord_seq'
    dic['coords'] = 'http://opengis.org/operations/coords'
    dic['count'] = 'http://opengis.org/operations/count'
    dic['crosses'] = 'http://opengis.org/operations/crosses'
    dic['crs'] = 'http://opengis.org/operations/crs'
    dic['difference'] = 'http://opengis.org/operations/difference'
    dic['dims'] = 'http://opengis.org/operations/dims'
    dic['disjoint'] = 'http://opengis.org/operations/disjoint'
    dic['distance'] = 'http://opengis.org/operations/distance'
    dic['empty'] = 'http://opengis.org/operations/empty'
    dic['envelope'] = 'http://opengis.org/operations/envelope'
    dic['equals'] = 'http://opengis.org/operations/equals'
    dic['equals_exact'] = 'http://opengis.org/operations/equals_exact'
    dic['ewkb'] = 'http://opengis.org/operations/ewkb'
    dic['ewkt'] = 'http://opengis.org/operations/ewkt'
    dic['extend'] = 'http://opengis.org/operations/extend'
    dic['extent'] = 'http://opengis.org/operations/extent'
    dic['geojson'] = 'http://opengis.org/operations/geojson'
    dic['geom_type'] = 'http://opengis.org/operations/geom_type'
    dic['geom_typeid'] = 'http://opengis.org/operations/geom_typeid'
    dic['get_coords'] = 'http://opengis.org/operations/get_coords'
    dic['get_srid'] = 'http://opengis.org/operations/get_srid'
    dic['get_x'] = 'http://opengis.org/operations/get_x'
    dic['get_y'] = 'http://opengis.org/operations/get_y'
    dic['get_z'] = 'http://opengis.org/operations/get_z'
    dic['has_cs'] = 'http://opengis.org/operations/has_cs'
    dic['hasz'] = 'http://opengis.org/operations/hasz'
    dic['hex'] = 'http://opengis.org/operations/hex'
    dic['hexewkb'] = 'http://opengis.org/operations/hexewkb'
    dic['index'] = 'http://opengis.org/operations/index'
    dic['intersection'] = 'http://opengis.org/operations/intersection'
    dic['intersects'] = 'http://opengis.org/operations/intersects'
    dic['interpolate'] = 'http://opengis.org/operations/interpolate'
    dic['json'] = 'http://opengis.org/operations/json'
    dic['kml'] = 'http://opengis.org/operations/kml'
    dic['length'] = 'http://opengis.org/operations/length'
    dic['normalize'] = 'http://opengis.org/operations/normalize'
    dic['num_coords'] = 'http://opengis.org/operations/num_coords'
    dic['num_geom'] = 'http://opengis.org/operations/num_geom'
    dic['num_s'] = 'http://opengis.org/operations/num_s'
    dic['num_points']  = 'http://opengis.org/operations/num_points'
    dic['point_on_surface'] = 'http://opengis.org/operations/point_on_surface'
    dic['ogr'] = 'http://opengis.org/operations/ogr'
    dic['overlaps'] = 'http://opengis.org/operations/overlaps'
    dic['_on_surface'] = 'http://opengis.org/operations/_on_surface'
    dic['pop'] = 'http://opengis.org/operations/pop'
    dic['prepared'] = 'http://opengis.org/operations/prepared'
    dic['relate'] = 'http://opengis.org/operations/relate'
    dic['relate_pattern'] = 'http://opengis.org/operations/relate_pattern'
    dic['ring'] = 'http://opengis.org/operations/ring'
    dic['set_coords'] = 'http://opengis.org/operations/set_coords'
    dic['set_srid'] = 'http://opengis.org/operations/set_srid'
    dic['set_x'] = 'http://opengis.or   g/operations/set_x'
    dic['set_y'] = 'http://opengis.org/operations/set_y'
    dic['set_z'] = 'http://opengis.org/operations/set_z'
    dic['simple'] = 'http://opengis.org/operations/simple'
    dic['simplify'] = 'http://opengis.org/operations/simplify'
    dic['srid'] = 'http://opengis.org/operations/srid'
    dic['srs'] = 'http://opengis.org/operations/srs'
    dic['sym_difference'] = 'http://opengis.org/operations/sym_difference'
    dic['touches'] = 'http://opengis.org/operations/touches'
    dic['transform'] = 'http://opengis.org/operations/transform'
    dic['tuple'] = 'http://opengis.org/operations/tuple'
    dic['union'] = 'http://opengis.org/operations/union'
    dic['valid'] = 'http://opengis.org/operations/valid'
    dic['valid_reason'] = 'http://opengis.org/operations/valid_reason'
    dic['within'] = 'http://opengis.org/operations/within'
    dic['wkb'] = 'http://opengis.org/operations/wkb'
    dic['wkt'] = 'http://opengis.org/operations/wkt'
    dic['x'] = 'http://opengis.org/operations/x'
    dic['y'] = 'http://opengis.org/operations/y'
    dic['z'] = 'http://opengis.org/operations/z'

    return dic

def vocabulary(a_key):

    return vocabularyDict()[a_key] if a_key in vocabularyDict() else None


class Type_Called():
    def __init__(self, a_name='', params=[], answer=None):
        self.name = a_name
        self.parameters = params
        self.return_type = answer


def geometry_operations():
    dic = {}
    if len(dic) == 0:
        dic['area'] = Type_Called('area', [], float)
        dic['boundary'] = Type_Called('boundary', [], float)
        dic['buffer'] = Type_Called('buffer', [float], GEOSGeometry)
        dic['centroid'] = Type_Called('centroid', [], Point)
        dic['contains'] = Type_Called('contains', [GEOSGeometry], bool)
        dic['convex_hull'] = Type_Called('convex_hull', [], Polygon)
        dic['coord_seq'] = Type_Called('coord_seq', [], tuple)
        dic['coords'] = Type_Called('coords', [], tuple)
        dic['count'] = Type_Called('count', [], int)
        dic['crosses'] = Type_Called('crosses', [GEOSGeometry], bool)
        from django.contrib.gis.gdal import SpatialReference

        dic['crs'] = Type_Called('crs', [], SpatialReference)
        dic['difference'] = Type_Called('difference', [GEOSGeometry], GEOSGeometry)
        dic['dims'] = Type_Called('dims', [], int)
        dic['disjoint'] = Type_Called('disjoint', [GEOSGeometry], bool)
        dic['distance'] = Type_Called('distance', [GEOSGeometry], float)
        dic['empty'] = Type_Called('empty', [], bool)
        dic['envelope'] = Type_Called('envelope', [], GEOSGeometry)
        dic['equals'] = Type_Called('equals', [GEOSGeometry], bool)
        dic['equals_exact'] = Type_Called('equals_exact', [GEOSGeometry, float], bool)
        dic['ewkb'] = Type_Called('ewkb', [], str)
        dic['ewkt'] = Type_Called('ewkt', [], str)
        dic['extend'] = Type_Called('extend', [], tuple)
        dic['extent'] = Type_Called('extent', [], tuple)
        dic['geojson'] = Type_Called('geojson', [], str)
        dic['geom_type'] = Type_Called('geom_type', [], str)
        dic['geom_typeid'] = Type_Called('geom_typeid', [], int)
        dic['get_coords'] = Type_Called('get_coords', [], tuple)
        dic['get_srid'] = Type_Called('get_srid', [], str)
        dic['get_x'] = Type_Called('get_x', [], str)
        dic['get_y'] = Type_Called('get_y', [], str)
        dic['get_z'] = Type_Called('get_z', [], str)
        dic['has_cs'] = Type_Called('has_cs', [], bool)
        dic['hasz'] = Type_Called('hasz', [], bool)
        dic['hex'] = Type_Called('hex', [], str)
        dic['hexewkb'] = Type_Called('hexewkb', [], str)
        dic['index'] = Type_Called('index', [], int)
        dic['intersection'] = Type_Called('intersection', [GEOSGeometry], GEOSGeometry)
        dic['intersects'] = Type_Called('intersects', [GEOSGeometry], bool)
        dic['interpolate'] = Type_Called('interpolate', [float], Point)
        dic['json'] = Type_Called('json', [], str)
        dic['kml'] = Type_Called('kml', [], str)
        dic['length'] = Type_Called('length', [], float)
        dic['normalize'] = Type_Called('normalize', [float], Point)
        dic['num_coords'] = Type_Called('num_coords', [], int)
        dic['num_geom'] = Type_Called('num_geom', [], int)
        dic['num_points'] = Type_Called('num_points', [], int)
        dic['ogr'] = Type_Called('ogr', [], OGRGeometry)
        dic['overlaps'] = Type_Called('overlaps', [GEOSGeometry], bool)
        dic['point_on_surface'] = Type_Called('point_on_surface', [], Point)
        # dic['pop'] = Type_Called('pop', [], tuple)
        # dic['prepared'] = Type_Called('prepared', [], PreparedGeometry)
        dic['relate'] = Type_Called('relate', [GEOSGeometry], str)
        dic['relate_pattern'] = Type_Called('relate_pattern', [GEOSGeometry, str], str)
        dic['ring'] = Type_Called('ring', [], bool)
        dic['set_coords'] = Type_Called('set_coords', [tuple], None)
        dic['set_srid'] = Type_Called('set_srid', [str], None)
        dic['set_x'] = Type_Called('set_x', [float], None)
        dic['set_y'] = Type_Called('set_y', [float], None)
        dic['set_z'] = Type_Called('set_z', [float], None)
        dic['simple'] = Type_Called('simple', [], bool)
        dic['simplify'] = Type_Called('simplify', [float, bool], GEOSGeometry)
        dic['srid'] = Type_Called('srid', [], int)
        dic['srs'] = Type_Called('srs', [], SpatialReference)
        dic['sym_difference'] = Type_Called('sym_difference', [GEOSGeometry], GEOSGeometry)
        dic['touches'] = Type_Called('touches', [GEOSGeometry], bool)
        dic['transform'] = Type_Called('transform', [int, bool], GEOSGeometry)
        # dic['tuple'] = Type_Called('tuple', [], tuple)
        dic['union'] = Type_Called('union', [GEOSGeometry], GEOSGeometry)
        dic['valid'] = Type_Called('valid', [GEOSGeometry], bool)
        dic['valid_reason'] = Type_Called('valid_reason', [GEOSGeometry], str)
        dic['within'] = Type_Called('within', [GEOSGeometry], bool)
        dic['wkb'] = Type_Called('wkb', [], str)
        dic['wkt'] = Type_Called('wkt', [], str)
        dic['x'] = Type_Called('x', [], float)
        dic['y'] = Type_Called('y', [], float)
        dic['z'] = Type_Called('z', [], float)
        return dic

def point_operations():
    dict = geometry_operations()
    return dict

def line_operations():
    dict = geometry_operations()
    return dict

def polygon_operations():
    dict = geometry_operations()
    return dict

    def description(self):
        param = self.parameters or []
        return "operation name:" + self.name + " " + "parameters:" + ",".join(param) + " " + "returned value:" + self.return_type

class SupportedProperty():
    def __init__(self, property_name='', required=False, readable=True, writeable=True, is_unique=False, is_identifier=False ):
        self.property_name = property_name
        self.required = required
        self.readable = readable
        self.writeable = writeable
        self.is_unique = is_unique
        self.is_identifier = is_identifier

class SupportedOperation():
    def __init__(self, operation='', title='', method='', expects='', returns='', type='', link=''):
        self.method = method
        self.operation = operation
        self.title = title
        self.expects = expects
        self.returns = returns
        self.type = type
        self.link= link

    def context(self):
        return {"hydra:method": self.method, "hydra:operation": self.operation, "hydra:expects": self.expects, "hydra:returns": self.returns, "hydra:statusCode": '', "@id": self.link}

def initialize_dict():
        dict = {}
        dict[GEOSGeometry] = geometry_operations()
        dict[Point] = point_operations()
        dict[Polygon] = polygon_operations()
        dict[LineString] = line_operations()
        dict[MultiPoint] = point_operations()
        dict[MultiPolygon] = polygon_operations()
        dict[MultiLineString] = line_operations()
        dict[GeometryCollection] = geometry_operations()
        return dict


class ContextResource:

    def __init__(self):
        self.basic_path = None
        self.host = None
        self.dict_context = None
        self.resource = None

    #def attribute_name_list(self):
    #    return ( field.attname for field in self.model_class._meta.fields[:])

    #def attribute_type_list(self):
    #    return ( type(field) for field in self.model_class._meta.fields[:])

    def operation_names(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and self.is_not_private(method)]

    def attribute_contextualized_dict_for(self, field):
        voc = vocabulary(field.name)
        res_voc = voc if voc is not None else vocabulary(type(field))
        return { "@id": res_voc, "@type": "@id"}


    def attributes_contextualized_dict(self):
        dic_field = {}
        for field_model in self.resource.fields_to_web:
            dic_field[field_model.name] = self.attribute_contextualized_dict_for(field_model)
        return dic_field


    def selectedAttributeContextualized_dict(self, attribute_name_array):

        return {k: v for k, v in self.attributes_contextualized_dict().iteritems() if k in attribute_name_array}

    def hydraSuportedProperties(self):
        arr = [];
        for  field in self.model_class._meta.fields:
            arr.append(self.hydraSuportedProperty(field.attname, True, True, False))
        return arr;

    def generateSuportedProperties(self):
        dic = {}
        dic["suportedProperty"] = self.hydraSuportedProperties()
        return dic

    def supportedProperties(self):
        arr_dic = [ ]
        return {arr_dic }

    def supportedOperations(self):
        arr_dic = [
            {"hydra:method": "GET","hydra:operation": "srs","hydra:expects":"", "hydra:returns": "",  "hydra:statusCode": ""},
            {"hydra:method": "GET","hydra:operation": "envelope","hydra:expects":"", "hydra:returns": "http://geojson.org/geojson-ld/vocab.html#geometry",  "hydra:statusCode": ""},
        ]
        return arr_dic
    def supportedOperationsFor(self, object):
        dict = initialize_dict()
        a_type = type(object)
        dict_operations = dict[a_type] if a_type in dict else {}
        arr = []
        for k, v_typed_called in dict_operations.iteritems():
            exps = [] if v_typed_called.parameters is None else [vocabulary(param) for param in v_typed_called.parameters]
            rets = (vocabulary(v_typed_called.return_type) if v_typed_called.return_type in vocabularyDict()  else ("NOT FOUND"))
            link_id = vocabulary(v_typed_called.name)
            arr.append( SupportedOperation(operation=v_typed_called.name, title=v_typed_called.name, method='GET', expects=exps, returns=rets, type='', link=link_id))

        return [supportedOperation.context() for supportedOperation in arr]

    def iriTemplates(self):
        return {}

    def set_context_to_attributes(self, attributes_name):
        self.dict_context = {}
        self.dict_context["@context"] = self.selectedAttributeContextualized_dict(attributes_name)

    def set_context_to_only_one_attribute(self, object, attribute_name):
        self.set_context_to_attributes([attribute_name])

        obj = getattr(object, attribute_name, None)
        isGeometry = isinstance(obj, GEOSGeometry)
        if isGeometry:
           self.dict_context["hydra:supportedOperations"] = self.supportedOperationsFor(obj)

    def set_context_to_operation(self, object, operation_name):
        self.dict_context = {}
        dict = {}
        dict [operation_name] = { "@id": vocabulary(operation_name),"@type": "@id" }
        self.dict_context["@context"] = dict
        isGeometry = isinstance(object, GEOSGeometry)
        if isGeometry:
            self.dict_context["hydra:supportedOperations"] = self.supportedOperationsFor(object)

    def set_context_to_object(self, object, attribute_name):
        self.dict_context = {}
        self.dict_context["@context"] = self.selectedAttributeContextualized_dict([attribute_name])
        if len(self.dict_context["@context"]) == 0:
            self.set_context_to_operation(object, attribute_name)
        else:
            self.dict_context["hydra:supportedOperations"] = self.supportedOperationsFor(object)

    def initalize_context(self):
        self.dict_context = {}
        self.dict_context["@context"] = self.attributes_contextualized_dict()
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