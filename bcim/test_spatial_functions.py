
from django.test import SimpleTestCase

import json
import httplib2
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
        self.host_base = "http://172.30.10.120:8000"
        self.url_uf_by_sigla = self.host_base + "/ibge/bcim/estados/RJ/"
        self.url_uf_by_geocodigo = self.host_base + "/ibge/bcim/estados/RJ/"
        self.h = httplib2.Http(".cache")

    def test_uf_sigla_contains_point(self):
        url = self.host_base + "/ibge/bcim/estados/RJ/contains/POINT(-42 -21)/"
        resp, gj = self.h.request(url, "GET")
        is_true = json.loads(gj.decode())["contains"]
        self.assertTrue(is_true)

