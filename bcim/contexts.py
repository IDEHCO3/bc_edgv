from hyper_resource.contexts import FeatureContext, FeatureCollectionContext

class UnidadeFederacaoContext(FeatureContext):

    def attributes_contextualized_dict(self):

        dic_context = {            "id_objeto": { "@id": "http://schema.org/identifier", "@type": "@id"},
                                   "nome": { "@id": "http://schema.org/name", "@type": "@id"},
                                   "nomeabrev": {"@id": "http://schema.org/alternateName"},
                                   "sigla": { "@id": "http://schema.org/alternateName", "@type": "@id"},
                                   "geometriaaproximada": { "@id": "http://schema.org/Boolean", "@type": "@id"},
                                   "geocodigo": { "@id": "http://schema.org/code", "@type": "@id"},
                                   "geom": {"@id": "http://geojson.org/geojson-ld/vocab.html#geometry", "@type": "@id"}
                       }

        return dic_context

    #def  supportedProperties(self):
    #dic = {"hydra:supportedProperties": [
    #    {
    #        "hydra:writeable": true, "hydra:property": "nome", "hydra:readable": true, "isIdentifier": false, "hydra:required": true, "isExternal": false, "@type": "SupportedProperty",  "isUnique": false
    #    }
    #]}
    #return dic


class MunicipioContext(FeatureContext):
    pass

class AldeiaIndigenaContext(FeatureContext):
    pass

class AldeiaIndigenaContext(FeatureContext):
    pass
