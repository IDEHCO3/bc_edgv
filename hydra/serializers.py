from hydra.hydra import *
from hydra.models import SupportedProperty, SupportedOperation
from context.models import Class

class HydraSerializer(HydraClassSerializer):

    def __init__(self, classobject, request, classname, spatial=None):
        super(HydraSerializer, self).__init__()
        self.request = request
        self.classobject = classobject
        self.class_name = classname
        self.properties_objects = SupportedProperty.objects.filter(hydra_class=classobject.id)
        self.operations_objects = SupportedOperation.objects.filter(hydra_class=classobject.id)
        self.spatial_operations = self.getSpatialOperations(spatial)

    def getSpatialOperations(self, spatial=None):
        if spatial == "geometry":
            geometry = Class.objects.filter(name="geometry")
            return SupportedOperation.objects.filter(hydra_class=geometry.id)
        return None

    def createProperties(self, property_serializer):
        for property in self.properties_objects:
            property_serializer.addProperty(name=property.property, required=property.required, readable=property.readable, writeable=property.writeable)

    def createMethods(self, method_serializer):
        for method in self.operations_objects:
            method_serializer.addCustomOperation(type=method.type, title=method.title, httpMethod=method.method, expects=self.getURLClass(method.expects), returns=self.getURLClass(method.returns))
        if self.spatial_operations is not None:
            for method in self.spatial_operations:
                method_serializer.addCustomOperation(type=method.type, title=method.title, httpMethod=method.method, expects=self.getURLClass(method.expects), returns=self.getURLClass(method.returns))

    def getURLClass(self, obj):
        if obj is not None:
            return reverse('context:detail', args=[obj.name], request=self.request)
        return ""