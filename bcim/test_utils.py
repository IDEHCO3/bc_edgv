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
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'bc_edgv.settings'

#python manage.py test bcim.test_utils  --testrunner=bcim.test_utils.NoDbTestRunner

class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass


#python manage.py test bcim.test_utils  --testrunner=bcim.test_utils.NoDbTestRunner
from django.test import SimpleTestCase
from bcim.utils import APIViewDetailSpatialFunction, APIViewBasicSpatialFunction


class APIViewBasicSpatialFunctionTestCase(SimpleTestCase):
    def setUp(self):
        self.dic1 = {'spatial_function_1': 'envelope',  'spatial_function_2': 'area', 'sigla': 'RJ' } #sp1 sp2 0 0
        self.api =  APIViewBasicSpatialFunction()

    def test_key_is_spatial_function(self):
        self.assertTrue(self.api.key_is_spatial_function('spatial_function_1'))
        self.assertTrue(self.api.key_is_spatial_function('spatial_function_2'))
        self.assertTrue(self.api.key_is_spatial_function('spatial_function_3'))
        self.assertFalse(self.api.key_is_spatial_function('sigla'))
        self.assertFalse(self.api.key_is_spatial_function('param_1'))
        self.assertFalse(self.api.key_is_spatial_function('param_2'))
        self.assertFalse(self.api.key_is_spatial_function('param_3'))

    def test_key_is_not_spatial_function(self):
        self.assertTrue(self.api.key_is_not_spatial_function('spatial_functiona_1'))

    def test_key_is_param(self):
        self.assertFalse(self.api.key_is_param('spatial_function_1'))
        self.assertFalse(self.api.key_is_param('spatial_function_2'))
        self.assertFalse(self.api.key_is_param('spatial_function_3'))
        self.assertFalse(self.api.key_is_param('sigla'))
        self.assertTrue(self.api.key_is_param('param_1'))
        self.assertTrue(self.api.key_is_param('param_2'))
        self.assertTrue(self.api.key_is_param('param_3'))

    def test_key_is_not_param(self):
        self.assertTrue(self.api.key_is_not_param('paramq_1'))

    def test_key_is_identifier(self):

        self.assertTrue(self.api.key_is_identifier('sigla'))
        self.assertFalse(self.api.key_is_identifier('param_1'))
        self.assertFalse(self.api.key_is_identifier('param_2'))
        self.assertFalse(self.api.key_is_identifier('param_3'))
        self.assertFalse(self.api.key_is_identifier('spatial_function_1'))
        self.assertFalse(self.api.key_is_identifier('spatial_function_2'))
        self.assertFalse(self.api.key_is_identifier('spatial_function_3'))
        self.assertFalse(self.api.key_is_identifier('function_1'))
        self.assertFalse(self.api.key_is_identifier('function_2'))
        self.assertFalse(self.api.key_is_identifier('function_3'))


class APIViewDetailSpatialFunctionTestCase(SimpleTestCase):
    def setUp(self):
        self.dic1 = {'spatial_function_1': 'envelope',  'spatial_function_2': 'area', 'sigla': 'RJ' } #sp1 sp2 0 0
        self.dic2 = {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'sigla': 'RJ' } #sp1 param1 sp2 0
        self.dic3 = {'spatial_function_1': 'envelope',  'spatial_function_2': 'transform', 'param_2': '3685&True', 'sigla': 'RJ' } #sp1 0 sp2 param2
        self.dic4 = {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'sigla': 'RJ' } #sp1 param1 sp2 param2
        self.dic5 = {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'spatial_function_3': 'buffer',  'sigla': 'RJ' }
        self.dic6 = {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'spatial_function_3': 'buffer', 'param_3': '2', 'sigla': 'RJ' }

        self.api =  APIViewDetailSpatialFunction()

    def test_spatial_functions_with_params(self):
        #dic1 {'spatial_function_1': 'envelope',  'spatial_function_2': 'area', 'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic1)
        boolean = dic['envelope']== None
        self.assertTrue(boolean)
        boolean = dic['area']== None
        self.assertTrue(boolean)
        self.assertIsNone(dic.get('sigla'))

        #dic2 {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic2)
        boolean = dic['transform']== '3685'
        self.assertTrue(boolean)
        boolean = dic['area']== None
        self.assertTrue(boolean)
        self.assertIsNone(dic.get('sigla'))

        #dic3 {'spatial_function_1': 'envelope',  'spatial_function_2': 'transform', 'param_2': '3685&True', 'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic3)
        boolean = dic['envelope']== None
        self.assertTrue(boolean)
        self.assertEqual(dic['transform'], '3685&True')
        self.assertIsNone(dic.get('sigla'))

        #dic4 {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic4)
        boolean = dic['transform']== '3685'
        self.assertTrue(boolean)
        self.assertEqual(dic['area'], 'KM')
        self.assertIsNone(dic.get('sigla'))

        #dic5 {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'spatial_function_3': 'buffer',  'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic5)
        boolean = dic['transform']== '3685'
        self.assertTrue(boolean)
        self.assertEqual(dic['area'], 'KM')
        self.assertIsNone(dic.get('sigla'))
        self.assertIsNone(dic['buffer'])
        #dic6 {'spatial_function_1': 'transform', 'param_1': '3685', 'spatial_function_2': 'area', 'param_2': 'KM', 'spatial_function_3': 'buffer', 'param_3': '2', 'sigla': 'RJ' }
        dic = self.api.spatial_functions_with_params(self.dic6)
        boolean = dic['transform']== '3685'
        self.assertTrue(boolean)
        self.assertEqual(dic['area'], 'KM')
        self.assertIsNone(dic.get('sigla'))
        self.assertEqual(dic['buffer'], '2')

    def test_dic_with_only_identitier_field(self):
        dic = self.api.dic_with_only_identitier_field(self.dic1)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)
        dic = self.api.dic_with_only_identitier_field(self.dic2)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)
        dic = self.api.dic_with_only_identitier_field(self.dic3)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)
        dic = self.api.dic_with_only_identitier_field(self.dic4)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)
        dic = self.api.dic_with_only_identitier_field(self.dic5)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)
        dic = self.api.dic_with_only_identitier_field(self.dic6)
        self.assertEqual(dic['sigla'], 'RJ')
        self.assertEqual(len(dic.items()), 1)

