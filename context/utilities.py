from rest_framework.reverse import reverse
from context.models import *
from context.serializers import *
from hydra.utilities import getHydraData

def createLinkOfContext(classname, request, response):
    response['Link'] = '<'+reverse('context:detail', args=[classname], request=request)+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\";'
    return response

def getContextData(classname, request):
    try:
        classobject = Class.objects.get(name=classname)
    except:
        return ""
    serializer = ContextSerializer(classobject)
    contextdata = serializer.data
    hydradata = getHydraData(classname, request)
    if "@context" in hydradata:
        hydradata["@context"].update(contextdata["@context"])
    contextdata.update(hydradata)
    return contextdata