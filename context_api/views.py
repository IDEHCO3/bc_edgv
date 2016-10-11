from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from context_api.models import *
from context_api.serializers import ContextSerializer
from hydra.serializers import HydraSerializer
from rest_framework import status

from context_api.utilities import *
# Create your views here.

class GeojsonOnContentType(object):

    def get(self, request, *args, **kwargs):
        response = super(GeojsonOnContentType, self).get(request, *args, **kwargs)
        if request.accepted_media_type != "text/html":
            response.content_type = "application/vnd.geo+json"
        return response


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

class BaseContext(object):

    def options(self, request, *args, **kwargs):
        classname = self.getClassName(request)
        response = Response(getContextData(classname, request), status=status.HTTP_200_OK, content_type="application/ld+json")
        response = createLinkOfContext(classname, request, response)
        return response

    def get(self, request, *args, **kwargs):
        response = super(BaseContext, self).get(request, *args, **kwargs)
        classname = self.getClassName(request)
        response = createLinkOfContext(classname, request, response)
        return response

    def getClassName(self, request):
        if not hasattr(self, 'classname'):
            classname = getClassnameByURL(request._request.path)
        else:
            classname = self.classname
        return classname

class CreatorContextList(generics.ListCreateAPIView, BaseContext):
    pass

class CreatorContextDetail(generics.RetrieveUpdateDestroyAPIView, BaseContext):
    pass



