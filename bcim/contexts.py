from hyper_resource.contexts import FeatureContext

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



    def iriTemplates(self):
        iri_templates = []
        dict = {}
        dict["@type"] = "IriTemplate"
        dict["template"] = self.host + self.basic_path + "{/list*}" #Ex.: http://host/unidades-federativas/nome,sigla,geom
        dict["mapping"] = [{"@type": "iriTemplateMapping", "variable":"list*", "property": "hydra:property", "required": True} ]
        iri_templates.append(dict)

        dict = {}
        dict["@type"] = "IriTemplate"
        dict["template"] = self.host + self.basic_path + "{/sigla}" #Ex.: http://host/unidades-federativas/sigla
        dict["mapping"] = [{"@type": "iriTemplateMapping", "variable":"sigla", "property": "hydra:property", "required": True} ]
        iri_templates.append(dict)

        dict = {}
        dict["@type"] = "IriTemplate"
        dict["template"] = self.host + self.basic_path + "{/geocodigo}"
        dict["mapping"] = [{"@type": "iriTemplateMapping", "variable":"geocodigo", "property": "hydra:property", "required": True} ]
        iri_templates.append(dict)

        return {"iri_templates": iri_templates}


