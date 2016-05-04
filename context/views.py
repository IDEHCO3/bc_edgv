from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from context.models import *

# Create your views here.

class ContextView(APIView):


    def get(self, request, *args, **kwargs):
        classname = kwargs.get('classname')
        pk = Class.objects.get(name=classname).id
        context = Context.objects.get(classname=pk)
        response = Response(data={"testando": "isso ai!"})
        if request.accepted_media_type != "text/html":
            response.content_type = "application/ld+json"
        return response