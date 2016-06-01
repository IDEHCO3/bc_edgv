from rest_framework.serializers import ModelSerializer
from context.context import ContextBase
from context.models import Context

class ContextSerializer(ContextBase):

    def __init__(self, data):
        self.model = Context
        for semantic in data:
            triple = self.getKeyValueTuple(semantic)
            if len(triple) == 3:
                self.addAttribute(triple[0], id=triple[1], type=triple[2])
            if len(triple) == 2:
                self.addAttribute(triple[0], url=triple[1])

    def getKeyValueTuple(self, obj):
        if obj.type is not None:
            return (obj.attribute, obj.means, obj.type)
        else:
            return (obj.attribute, obj.means)


