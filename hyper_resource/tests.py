import django
import rest_framework
#from rest_framework import generics
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from rest_framework import permissions
#from rest_framework import permissions

from django.contrib.gis.geos import Point
from django.test import TestCase
# Create your tests here.
from django.contrib.gis.db import models

from hyper_resource.models import FeatureModel, point_operations, geometry_operations
from hyper_resource.views import AbstractResource
from django.contrib.gis.geos import GEOSGeometry
from django.test import SimpleTestCase

import json
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from django.test.runner import DiscoverRunner
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'bc_edgv.settings'
#django.setup()
#python manage.py test bcim.test_utils  --testrunner=bcim.test_utils.NoDbTestRunner

class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass

class Ponto(FeatureModel):
    id_objeto = models.IntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
class Linha(FeatureModel):
    id_objeto = models.IntegerField(primary_key=True)
    geom = models.LineStringField(blank=True, null=True)
class Poligono(FeatureModel):
    id_objeto = models.IntegerField(primary_key=True)
    geom = models.PolygonField(blank=True, null=True)
class Geometria(FeatureModel):
    id_objeto = models.IntegerField(primary_key=True)
    geom = models.GeometryField(blank=True, null=True)

## ativando virtual environment em: source ~/desenv/env/env_bc_edgv/bin/activate
## Testando
# python manage.py test hyper_resource.tests  --testrunner=hyper_resource.tests.NoDbTestRunner
##
#python manage.py test bcim.test_utils  --testrunner=bcim.test_utils.NoDbTestRunner
from django.test import SimpleTestCase
#from bcim.utils import APIViewHypermedia
#python manage.py test app --testrunner=app.filename.NoDbTestRunner
#python manage.py test bcim.tests  --testrunner=bcim.tests.NoDbTestRunner
#python manage.py test bcim.test_spatial_functions  --testrunner=bcim.test_spatial_functions.NoDbTestRunner


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


class FeatureModelTestCase(SimpleTestCase):
    def setUp(self):
        self.ponto = Ponto()
        self.linha = Linha()
        self.poligono = Poligono()
        self.geometria = Geometria()

    def url_feature(self):
        return ''

    def test_get_geometry_type(self):
        self.assertEquals(self.ponto.get_geometry_type(), Point)

    def test_operations_with_parameters_type(self):
        self.assertEquals(self.ponto.operations_with_parameters_type().keys(), point_operations().keys())

    def test_fields(self):
        self.assertEquals(self.ponto.fields()[0].name, 'id_objeto')
class AbstractResourceTestCase(SimpleTestCase):

    def setUp(self):
        self.tr = TesteResource('name', 'parameters', 'answer')

    def test_attributes(self):
        pass
    def test_operations(self):
        pass


class SpatialResourceTest(SimpleTestCase):

    def test_attributeContextualized(self):
        pass

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
