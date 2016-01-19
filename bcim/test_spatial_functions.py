
from django.test import SimpleTestCase

import json
import requests
from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import permissions
from django.test.runner import DiscoverRunner

class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass

#python manage.py test app --testrunner=app.filename.NoDbTestRunner
#python manage.py test bcim.tests  --testrunner=bcim.tests.NoDbTestRunner

class UnidadeFederacaoDetailSpatialQueryTestCase(SimpleTestCase):

    def setUp(self):
        self.json_type = type('str')
        self.host_base = 'http://172.30.10.120:8000'



    def test_uf_sigla_contains_point(self):
        an_url = url = self.host_base + '/ibge/bcim/estados/RJ/contains/POINT(-42 -21)/'
        req = requests.get(an_url)
        is_true = req.json()["contains"]
        self.assertTrue(is_true)

    def test_uf_sigla_contains_point_as_geojson(self):
        an_url = url = self.host_base + '/ibge/bcim/estados/RJ/contains/{ "type": "Point", "coordinates": [ -42, -21]}/'
        req = requests.get(an_url)
        is_true = req.json()["contains"]
        self.assertTrue(is_true)
"""
class UnidadeFederacaoListSpatialQueryTestCase(SimpleTestCase):
    def test_uf_sigla_contains_point(self):
        an_url = 'http://172.30.10.120:8000/ibge/bcim/aldeias-indigenas/'
        req = requests.get(an_url)
        value = json.loads(req.json())["type"]
        self.assertEquals(value,'FeatureCollection')
"""