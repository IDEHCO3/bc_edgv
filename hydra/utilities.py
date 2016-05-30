from context.models import *
from hydra.models import *
from hydra.serializers import *

def getHydraData(classname, request, spatial=None):
    classobject = Class.objects.get(name=classname)
    serializerHydra = HydraSerializer(classobject, request, classname, spatial)
    return serializerHydra.data
