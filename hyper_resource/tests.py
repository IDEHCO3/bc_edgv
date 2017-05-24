from django.test import TestCase

# Create your tests here.
from django.test.runner import DiscoverRunner
from django.contrib.gis.db import models

from hyper_resource.views import AbstractResource
from django.contrib.gis.geos import GEOSGeometry
from django.test import SimpleTestCase

class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass


class ModelTest(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipopostofisc = models.CharField(max_length=22, blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)
    polygon = models.PolygonField(blank=True, null=True)
    lineString = models.LineStringField(blank=True, null=True)
    point = models.PointField(blank=True, null=True)
    multipolygon = models.MultiPolygonField(blank=True, null=True)

class TesteResource(AbstractResource):
    def __init__(self, a_name, params, answer):
        self.name = a_name
        self.parameters = params
        self.return_type = answer

class AbstractResourceTestCase(SimpleTestCase):

    def setUp(self):
        tr = TesteResource('name', 'parameters', 'answer')

    def test_attributes(self):
        self.assertTrue( 'name' in self.tr.attribute_names())
        self.assertTrue('parameters' in self.tr.attribute_names())

    def test_operations(self):
        self.assertTrue('__init__' not in self.tr.operation_names())


class SpatialResourceTest(SimpleTestCase):

    def test_attributeContextualized(self):
        field = ModelTest._meta.fields[0]
        self.assertTrue('id_objeto' == field.name)
        dic = {'id_objeto': { "@id": "http://schema.org/identifier", "@type": "@id"}}


