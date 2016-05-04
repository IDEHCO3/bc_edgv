from rest_framework.metadata import BaseMetadata

class ContextBase(BaseMetadata):

    _data = {"@context": {}}

    def getTypeID(self):
        return "@id"

    def getTypeProductID(self):
        return "http://schema.org/productID"

    def getTypeBoolean(self):
        return "http://schema.org/Boolean"

    def getTypeFloat(self):
        return "http://schema.org/Float"

    def getTypeInteger(self):
        return "http://schema.org/Integer"

    def getTypeString(self):
        return "http://schema.org/Text"

    def getTypeDate(self):
        return "http://schema.org/Date"

    def getTypeDateTime(self):
        return "http://schema.org/DateTime"

    def getTypeTime(self):
        return "http://schema.org/Time"

    def getTypeGeometry(self):
        return "http://schema.org/GeoShape"

    def addAttribute(self, name, url=None, id=None, type=None):
        if url is not None:
            self._data["@context"][name] = url
        else:
            self._data["@context"][name] = {"@id": id, "@type": type}

    def determine_metadata(self, request, view):
        self.request = request
        return self.data

    def createOperations(self):
        if hasattr(self, "operation_class") and self.operation_class is not None:
            op = self.operation_class(request=self.request)
            self._data["suportedClass"] = op.data

    @property
    def data(self):
        self.createAttributes()
        self.createOperations()
        return self._data

    def createAttributes(self):
        pass