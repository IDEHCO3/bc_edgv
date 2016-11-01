from rest_framework.reverse import reverse
from context_api.models import *
from context_api.serializers import *
from hydra.utilities import getHydraData

def createLinkOfContext(classname, request, response, properties=None):
    if properties is None:
        url = reverse('context:detail', args=[classname], request=request)
    else:
        url = reverse('context:detail-property', args=[classname, ",".join(properties)], request=request)

    response['Link'] = '<'+url+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\";'
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

def getClassnameByURL(request, *args, **kwargs):
    path = request._request.path
    if path[-1] != '/':
            path += '/'
    list_path = path.split('/')
    classname = ""
    kwargs_list = [x[1] for x in kwargs.items()]
    for i in range(len(list_path)):
        e = list_path[i]
        if e in args or e in kwargs_list:
            if i > 0:
                classname = list_path[i-1]
                break
    if classname == "":
        size = len(list_path)
        if list_path[size-1] == '':
            classname = list_path[-2]
        else:
            classname = list_path[-1]
    return classname