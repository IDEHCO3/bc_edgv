from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from context.models import *
from context.serializers import ContextSerializer
# Create your views here.

class ContextView(APIView):


    def get(self, request, *args, **kwargs):
        classname = kwargs.get('classname')
        pk = Class.objects.get(name=classname).id
        context = Context.objects.filter(classname=pk)

        serializer = ContextSerializer(context)
        response = Response(data=serializer.data)
        if request.accepted_media_type != "text/html":
            response.content_type = "application/ld+json"
        return response