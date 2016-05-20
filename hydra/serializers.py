from hydra.hydra import *
from hydra.models import SupportedProperty, SupportedOperation

class HydraSerializer(HydraClassSerializer):

    def __init__(self, classobject, request):
        super(HydraSerializer, self).__init__(request)
        self.classobject = classobject
        self.properties_objects = SupportedProperty.objects.filter(hydra_class=classobject.id)
        self.operations_objects = SupportedOperation.objects.filter(hydra_class=classobject.id)

    def createProperties(self, property_serializer):
        for property in self.properties_objects:
            pass

    def createMethods(self, method_serializer):
        for method in self.operations_objects:
            pass