from context.models import *
from hydra.models import *
from hydra.serializers import *

def getHydraData(classname, request):
    classobject = Class.objects.get(name=classname)
    serializerHydra = HydraSerializer(classobject, request, classname)
    return serializerHydra.data
