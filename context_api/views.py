from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from context_api.models import *
from context_api.serializers import ContextSerializer
from hydra.serializers import HydraSerializer
from rest_framework import status
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

    def __init__(self, contextclassname, serializer_object=None):
        self.serializer_object = serializer_object
        self.contextclassname = contextclassname

    def options(self, request):
        response = Response(self.getContextData(request), status=status.HTTP_200_OK, content_type="application/ld+json")
        response = self.createLinkOfContext(request, response)
        return response

    def addContext(self, request, response):
        return self.createLinkOfContext(request, response)

    def createLinkOfContext(self, request, response, properties=None):
        # if properties is None:
        #     url = reverse('context:detail', args=[self.contextclassname], request=request)
        # else:
        #     url = reverse('context:detail-property', args=[self.contextclassname, ",".join(properties)], request=request)
        url = request.build_absolute_uri()
        url = url if url[-1] != '/' else url[:-1]
        url = url + ".jsonld"

        context_link = ' <'+url+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\" '
        if "Link" not in response:
            response['Link'] = context_link
        else:
            response['Link'] += "," + context_link

        return response

    def getHydraData(self, request):
        classobject = Class.objects.get(name=self.contextclassname)
        serializerHydra = HydraSerializer(classobject, request)
        return serializerHydra.data

    def addIriTamplate(self, context, request, serializer_object):
        url = request.build_absolute_uri()
        iriTemplate = {
            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
            "@type": "IriTemplate",
            "template": url if url[-1] != '/' else url[:-1] +"{/attribute}",
            "variableRepresentation": "BasicRepresentation",
            "mapping": []
        }
        if serializer_object is not None:
            for attr in serializer_object.Meta.identifiers:
                iriTemplate['mapping'].append({
                    "@type": "IriTemplateMapping",
                    "variable": "attribute",
                    "property": attr,
                    "required": True
                })
        else:
            iriTemplate['mapping'].append({
                "@type": "IriTemplateMapping",
                "variable": "attribute",
                "property": "hydra:supportedProperties",
                "required": True
            })

        context['iriTemplate'] = iriTemplate
        return context

    def getContextData(self, request):
        try:
            classobject = Class.objects.get(name=self.contextclassname)
        except:
            return ""
        serializer = ContextSerializer(classobject)
        contextdata = serializer.data
        hydradata = self.getHydraData(request)
        if "@context" in hydradata:
            hydradata["@context"].update(contextdata["@context"])
        contextdata.update(hydradata)
        contextdata = self.addIriTamplate(contextdata, request, self.serializer_object)
        return contextdata






