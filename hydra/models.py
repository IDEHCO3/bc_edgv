from django.db import models
from django.contrib.gis.geos import GEOSGeometry, Point, LineString, Polygon
from context.models import Class
# Create your models here.

class SupportedProperty(models.Model):
    type = models.CharField(max_length=100, blank=False, null=False)
    property = models.CharField(max_length=100, blank=False, null=False)
    required = models.BooleanField(null=False)
    readable = models.BooleanField(null=False)
    writeable = models.BooleanField(null=False)
    hydra_class = models.ForeignKey(Class, blank=False, null=False, related_name='supported_properties')

class SupportedOperation(models.Model):
    type = models.CharField(max_length=100, blank=True, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    method = models.CharField(max_length=100, blank=False, null=False)
    returns = models.CharField(max_length=100, blank=True, null=False)
    possibleStatus = models.CharField(max_length=100, blank=True, null=True)
    hydra_class = models.ForeignKey(Class, blank=False, null=False, related_name='supported_operations')

class ExpectedParameter(models.Model):
    classname = models.ForeignKey(Class, blank=False, null=True)
    supportedOperation = models.ForeignKey(SupportedOperation, blank=False, null=False, related_name='expects')


def point_with_parameters_type():
    #dic = [   '', '', 'intersects', 'json', 'kml', 'length', 'normalize', 'num_coords', 'num_geom', 'num_points', 'ogr', 'overlaps', 'point_on_surface', 'pop', 'prepared', 'ptr', 'ptr_type', 'relate', 'relate_pattern', 'remove', 'reverse', 'ring', 'set_coords', 'set_srid', 'set_x', 'set_y', 'set_z', 'simple', 'simplify', 'sort', 'srid', 'srs', 'sym_difference', 'touches', 'transform', 'tuple', 'union', 'valid', 'valid_reason', 'within', 'wkb', 'wkt', 'x', 'y', 'z']
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









