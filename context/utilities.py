from rest_framework.reverse import reverse
from context.models import *
from context.serializers import *

def createLinkOfContext(classname, request, response):
    response['Link'] = '<'+reverse('context:detail', args=[classname], request=request)+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\";'
    return response

def getContextData(classname):
    pk = Class.objects.get(name=classname).id
    context = Context.objects.filter(classname=pk)
    serializer = ContextSerializer(context)
    return serializer.data