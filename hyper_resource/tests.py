from django.test import TestCase
# Create your tests here.
from django.test.runner import DiscoverRunner
from django.contrib.gis.db import models
from hyper_resource.views import AbstractResource
from django.contrib.gis.geos import GEOSGeometry
from django.test import SimpleTestCase

import json
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import permissions



class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass

#python manage.py test app --testrunner=app.filename.NoDbTestRunner
#python manage.py test bcim.tests  --testrunner=bcim.tests.NoDbTestRunner
#python manage.py test bcim.test_spatial_functions  --testrunner=bcim.test_spatial_functions.NoDbTestRunner

class DetailTestCase(SimpleTestCase):
    def setUp(self):
        self.json_type = type('str')
        self.host_base = 'http://172.30.10.61:8000'
        #self.host_base = 'http://127.0.0.1:8001'
        self.featureString = 'Feature'
        self.polygonString = 'Polygon'
        self.pointString = 'Point'
        self.multilineString = 'MultiLineString'
        self.lineString = 'LineString'
    def url_feature(self):
        return ''

    def test_feature(self):
        if len(self.url_feature())==0:
            return True
        an_url = self.host_base + self.url_feature()
        req = requests.get(an_url)
        self.assertEquals(req.json()['type'], self.featureString)

class UnidadeFederacaoDetailSpatialQueryTestCase(EDGVDetailTestCase):
    #testa se uma feature(multipoligon) contém um ponto dado em WKT
    def test_uf_sigla_contains_point(self):
        an_url = self.host_base + '/instituicoes/ibge/bcim/unidades-federativas/RJ/contains/POINT(-42 -21)/'
        req = requests.get(an_url)
        is_true = req.json().values().__iter__().__next__()== True
        self.assertTrue(is_true)
    #testa se uma feature(multipolygon) contém um ponto dado em geojson
    def test_uf_sigla_contains_point_as_geojson(self):
        an_url = self.host_base + '/instituicoes/ibge/bcim/unidades-federativas/RJ/contains/{ "type": "Point", "coordinates": [ -42, -21]}/'
        req = requests.get(an_url)
        is_true = req.json().values().__iter__().__next__()== True
        self.assertTrue(is_true)


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


class FeatureResourceTest(SimpleTestCase):

    def test_basic_get(self):
        pass
    def test_options_url_without_parameters(self):
        pass
    def test_options_url_with_only_attributes(self):
        pass
    def test_options_url_with_only_one_attribute(self):
        pass
    def test_options_url_with_spatia_functions(self):
        pass
