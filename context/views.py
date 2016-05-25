from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from context.models import *
from context.serializers import ContextSerializer
from hydra.utilities import getHydraData
# Create your views here.

class ContextView(APIView):


    def get(self, request, *args, **kwargs):
        classname = kwargs.get('classname')
        try:
            pk = Class.objects.get(name=classname).id
        except:
            return Response(data={})
        context = Context.objects.filter(classname=pk)

        serializer = ContextSerializer(context)
        contextdata = serializer.data
        hydradata = getHydraData(classname, request)
        if "@context" in hydradata:
            hydradata["@context"].update(contextdata["@context"])
        contextdata.update(hydradata)
        response = Response(data=contextdata)
        if request.accepted_media_type != "text/html":
            response.content_type = "application/ld+json"
        return response