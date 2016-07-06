from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from context.models import *
from context.serializers import ContextSerializer
from hydra.serializers import HydraSerializer
from rest_framework import status

from context.utilities import *
# Create your views here.

class ContextView(APIView):


    def get(self, request, *args, **kwargs):
        classname = kwargs.get('classname')
        try:
            classobject = Class.objects.get(name=classname)
        except:
            return Response(data={})

        contextdata = ContextSerializer(classobject).data
        hydradata = HydraSerializer(classobject, request).data
        if "@context" in hydradata:
            hydradata["@context"].update(contextdata["@context"])
        contextdata.update(hydradata)
        response = Response(data=contextdata)
        if request.accepted_media_type != "text/html":
            response.content_type = "application/ld+json"
        return response

class CreatorContext(generics.ListCreateAPIView):

    def options(self, request, *args, **kwargs):
        path = request._request.path
        if path[-1] != '/':
            path += '/'
        list_path = path.split('/')
        classname = list_path[len(list_path)-2]
        response = Response(getContextData(classname, request), status=status.HTTP_200_OK, content_type="application/ld+json")
        response = createLinkOfContext(classname, request, response)
        return response

    def get(self, request, *args, **kwargs):
        response = super(CreatorContext, self).get(request, *args, **kwargs)
        path = request._request.path
        if path[-1] != '/':
            path += '/'
        list_path = path.split('/')
        classname = list_path[-2]
        response = createLinkOfContext(classname, request, response)
        return response