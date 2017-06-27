from datetime import date, datetime, time
from django.contrib.gis.db import models
from django.contrib.gis.db.models import Q
# Create your models here.
from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import GeometryCollection
from django.contrib.gis.geos import LineString
from django.contrib.gis.geos import MultiLineString
from django.contrib.gis.geos import MultiPoint
from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos.prepared import PreparedGeometry

from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models import LineStringField
from django.contrib.gis.db.models import MultiLineStringField
from django.contrib.gis.db.models import MultiPointField
from django.contrib.gis.db.models import MultiPolygonField
from django.contrib.gis.db.models import PointField
from django.contrib.gis.db.models import PolygonField

def dict_field_to_type():
    d = {}
    d[models.CharField] = str
    d[models.TextField] = str
    d[models.IntegerField] = int
    d[models.FloatField] = float
    d[models.TimeField] = time
    d[models.DateTimeField] = datetime
    d[models.DateField] = date
    d[GeometryField] = GEOSGeometry
    d[LineStringField] = LineString
    d[MultiLineStringField] = MultiLineString
    d[MultiPointField] = MultiPoint
    d[MultiPolygonField] = MultiPolygon
    d[PointField] = Point
    d[PolygonField] = Polygon

    return d
def dict_map_geo_field_geometry():
    dic = {}
    dic[GeometryField] = GEOSGeometry
    dic[LineStringField] = LineString
    dic[MultiLineStringField] = MultiLineString
    dic[MultiPointField] = MultiPoint
    dic[MultiPolygonField] = MultiPolygon
    dic[PointField] = Point
    dic[PolygonField] = Polygon
    return dic

class Type_Called():
    def __init__(self, a_name='', params=[], answer=None):
        self.name = a_name
        self.parameters = params
        self.return_type = answer

class ConverterType():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConverterType, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def convert_to_string(self, value_as_str):
        return value_as_str

    def convert_to_int(self, value_as_str):
        return int(value_as_str)

    def convert_to_float(self, value_as_str):
        return float(value_as_str)

    def convert_to_date(self, value_as_str):
        return datetime.datetime.strptime(value_as_str, "%Y-%m-%d").date()

    def convert_to_datetime(self, value_as_str):
        return datetime.datetime.strptime(value_as_str, "%Y-%m-%d %H:%M:%S")

    def convert_to_time(self, value_as_str):
        return datetime.time.strptime(value_as_str, "%Y-%m-%d %H:%M:%S")

    def convert_to_geometry(self, value_as_str):
        pass

    def operation_to_convert_value(self, a_type):
        d = {}
        d[str] = self.convert_to_string
        d[int] = self.convert_to_int
        d[float] = self.convert_to_float
        d[date] = self.convert_to_date
        d[datetime] = self.convert_to_datetime
        d[time] = self.convert_to_time
        d[models.CharField] = self.convert_to_string
        d[models.TextField] = self.convert_to_string
        d[models.IntegerField] = self.convert_to_int
        d[models.FloatField] = self.convert_to_float
        d[models.TimeField] = self.convert_to_time
        d[models.DateTimeField] = self.convert_to_datetime
        d[models.DateField] = self.convert_to_date
        d[GeometryField] = self.convert_to_geometry

        return d[a_type]

    def value_converted(self, a_type, value):
        object_method = self.operation_to_convert_value(a_type)
        return object_method(value)

class QObjectFactory:

    def __init__(self, model_class, attribute_name, operation_or_operator, raw_value_as_str):
        self.model_class = model_class
        self.attribute_name = attribute_name
        self.operation_or_operator = operation_or_operator
        self.raw_value_as_str = raw_value_as_str

    def fields(self):
        return self.model_class._meta.fields

    def field_type(self):
        for field in self.fields():
            if field.name == self.attribute_name:
                return type(field)
        return None

    def convert_value_for(self, a_value):
        converter = ConverterType()
        return converter.value_converted(self.field_type(), a_value)

    def q_object_for_in(self):
        dc = {}
        arr_value = self.raw_value_as_str.split(',')
        arr_value_converted = [ self.convert_value_for(a_value) for a_value in arr_value]
        dc[self.attribute_name + '__in'] = arr_value_converted
        return Q(**dc)

    def q_object_for_eq(self):
        dc = {}
        dc[self.attribute_name] = self.convert_value_for(self.raw_value_as_str)
        return Q(**dc)

    def q_object_for_neq(self):
        dc = {}
        dc[self.attribute_name] = self.convert_value_for(self.raw_value_as_str)
        return ~Q(**dc)

    def q_object_for_between(self):
        dc = {}
        arr_value = self.raw_value_as_str.split(',')
        arr_value_converted = [self.convert_value_for(a_value) for a_value in arr_value]
        dc[self.attribute_name + '__range'] = arr_value_converted
        return Q(**dc)

    def q_object_operation_or_operator_in_dict(self):
        d = {}
        d['in'] = self.q_object_for_in
        d['eq'] = self.q_object_for_eq
        d['neq'] = self.q_object_for_neq
        d['between'] = self.q_object_for_between
        return d[self.operation_or_operator]

    def q_object(self):
        object_method = self.q_object_operation_or_operator_in_dict()
        return object_method()

class FactoryComplexQuery:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FactoryComplexQuery, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def fields(self, model_class):
        return model_class._meta.fields

    def field_names(self, mode_class):
        return [field.name for field in self.fields(mode_class)]

    def base_operators(self):
        return ['neq', 'eq','lt','lte','gt','gte','between','isnull','like','notlike','in','notin']

    def logical_operators(self):
        return ['or', 'and']

    def is_attribute(self, att_name, model_class):
        return att_name in self.field_names(model_class)

    def is_logical_operators(self, op):
       return op.lower() in self.logical_operators()

    def is_logical_operator_and_not_attribute(self, model_class, att_or_op):
       return self.is_logical_operators(att_or_op) and self.is_attribute(att_or_op, model_class)

    def q_object_with_logical_operator(self, q_object_expression_or_none, q_object, logical_operator_str):
        if q_object_expression_or_none is None:
            return q_object
        print(logical_operator_str.lower())
        print(logical_operator_str.lower() == 'and')
        return (q_object_expression_or_none & q_object) if logical_operator_str.lower() == 'and' else (q_object_expression_or_none | q_object)

    def expression_as_array_of_qbject(self, model_class, q_object_as_array, expression_as_array):
        if len(expression_as_array) == 0:
           return q_object_as_array

        att_name = expression_as_array[0]
        oper = expression_as_array[1]
        value = expression_as_array[2]
        qof = QObjectFactory(model_class, att_name, oper, value)
        q_object_as_array.append(qof.q_object())
        self.expression_as_array_of_qbject(model_class,expression_as_array[3:])

    def q_object_for_filter_expression(self, q_object_or_none, model_class, expression_as_array):
        #'sigla/in/rj,es,go/and/data/between/2017-02-01,2017-06-30/' = ['sigla','in','rj,es,go','and','data', 'between','2017-02-01,2017-06-30']
        if len(expression_as_array)  < 3:
            return q_object_or_none

        if self.is_attribute(expression_as_array[0], model_class):
            qof = QObjectFactory(model_class, expression_as_array[0], expression_as_array[1], expression_as_array[2])
            oper = qof.operation_or_operator
        else:
            qof = QObjectFactory(model_class, expression_as_array[1], expression_as_array[2], expression_as_array[3])
            oper = expression_as_array[0]

        q_object_expression = self.q_object_with_logical_operator(q_object_or_none, qof.q_object(), oper)

        return self.q_object_for_filter_expression(q_object_expression, model_class, expression_as_array[3:])


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

def collection_operations():
    dic = {}
    dic['filter'] = Type_Called('filter', [Q], object)
    dic['map'] = Type_Called('map', [Q], object)
    dic['annotate'] = Type_Called('annotate', [Q], object)
    return dic

def feature_collection_operations():

    return dict(collection_operations(), **geometry_operations())

def dict_geometry_operations():
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

class AbstractFeatureModel(models.Model):


    def model_class(self):
        return type(self)

    def _key_is_identifier(self, key):
        return key in self.serializer_class.Meta.identifiers

    def dic_with_only_identitier_field(self, dict_params):
        dic = dict_params.copy()
        a_dict = {}
        for key, value in dic.items():
            if self._key_is_identifier(key):
                a_dict[key] = value

        return a_dict

    def operation_names(self):
        method_names = dir(self)
        method_names.remove('objects')  # with objects the system breaks
        return [method_name for method_name in method_names if self.is_not_private(method_name) and callable(getattr(self, method_name)) ]

    def attribute_names(self):
        return [ attribute for attribute in dir(self) if not callable(getattr(self, attribute)) and self.is_not_private(attribute)]

    def fields(self):
        return self.model_class()._meta.fields

    def field_names(self):
        return [field.name for field in self.fields()]

    def is_private(self, attribute_or_method_name):
        return attribute_or_method_name.startswith('__') and attribute_or_method_name.endswith('__')

    def is_not_private(self, attribute_or_method_name):
        return not self.is_private(attribute_or_method_name)

    def is_operation(self, operation_name):
        return operation_name in self.operation_names()

    def is_attribute(self, attribute_name):
        return attribute_name in self.field_names()

        #return (attribute_name in dir(self) and not callable(getattr(self, attribute_name)))

    def operations_with_parameters_type(self):
        pass

    class Meta:
        abstract = True

class FeatureModel(AbstractFeatureModel):

    class Meta:
        abstract = True

    def geo_field(self):
        return [field for field in self.fields()  if  isinstance(field, GeometryField)][0]

    def geo_field_name(self):
        return self.geo_field().name

    def _get_geometry_object(self):
        return getattr(self, self.geo_field_name(), None)

    def _get_type_geometry_object(self):
        geo_object =  self._get_geometry_object()
        if geo_object is None:
            return None
        return type(geo_object)

    def get_geometry_type(self):
        geoType = self._get_type_geometry_object()
        return geoType if geoType is not None else dict_map_geo_field_geometry()[type(self.geo_field())]


    def operations_with_parameters_type(self):
        return dict_geometry_operations()[self.get_geometry_type()]

