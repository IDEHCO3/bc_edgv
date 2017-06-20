
from django.contrib.gis.db import models
# Create your models here.
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

class AbstractFeatureModel(models.Model):


    def _model_class(self):
        return self.serializer_class.Meta.model

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

    def is_private(self, attribute_or_method_name):
        return attribute_or_method_name.startswith('__') and attribute_or_method_name.endswith('__')

    def is_not_private(self, attribute_or_method_name):
        return not self.is_private(attribute_or_method_name)

    def is_operation(self, operation_name):
        return operation_name in self.operation_names()

    def is_attribute(self, attribute_name):
        return (attribute_name in dir(self) and not callable(getattr(self, attribute_name)))

    class Meta:
        abstract = True

class FeatureModel(AbstractFeatureModel):

    class Meta:
        abstract = True

    def _geo_field_name(self):
        return 'geom'

    def _get_geometry_object(self):
        return getattr(self, self._geo_field_name(), None)

    def _get_type_geometry_object(self):
        return type(self._get_geometry_object())

    def operations_with_parameters_type(self):
        return initialize_dict()[self._get_type_geometry_object()]

