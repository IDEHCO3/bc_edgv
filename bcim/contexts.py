from hyper_resource.contexts import ContextResource

class UnidadeFederacaoContext(ContextResource):

    def attributeContextualized_dict(self):

        dic_context = {"id_objeto": { "@id": "http://schema.org/identifier", "@type": "@id"},
                                   "nome": { "@id": "http://schema.org/name", "@type": "@id"},
                                   "nomeabrev": {"@id": "http://schema.org/alternateName"},
                                   "sigla": { "@id": "http://schema.org/alternateName", "@type": "@id"},
                                   "geometriaaproximada": { "@id": "http://schema.org/Boolean", "@type": "http://schema.org/Text"},
                                   "geocodigo": { "@id": "http://schema.org/code", "@type": "@id"},
                                   "geom": {"@id": "http://geojson.org/geojson-ld/vocab.html#geometry", "@type": "@id"}
                       }

        return dic_context


    def supportedProperties(self):
        arr_dic = [
            {"@type": "SupportedProperty", "hydra:property": "id_objeto","hydra:writeable": True, "hydra:readable": True,"hydra:required": True},
            {"@type": "SupportedProperty", "hydra:property": "nome","hydra:writeable": True, "hydra:readable": True,"hydra:required": True},
            {"@type": "SupportedProperty", "hydra:property": "nomeabrev","hydra:writeable": True, "hydra:readable": True,"hydra:required": False},
            {"@type": "SupportedProperty", "hydra:property": "sigla","hydra:writeable": True, "hydra:readable": True,"hydra:required": True},
            {"@type": "SupportedProperty", "hydra:property": "geometriaaproximada","hydra:writeable": True, "hydra:readable": True,"hydra:required": False},
            {"@type": "SupportedProperty", "hydra:property": "geocodigo","hydra:writeable": True, "hydra:readable": True,"hydra:required": True},
            {"@type": "SupportedProperty", "hydra:property": "geom","hydra:writeable": True, "hydra:readable": True,"hydra:required": True},

        ]
        return arr_dic

    def supportedOperations(self):
        arr_dic = [
            {"@id": "http://opengis.org/operations/srs","hydra:method": "GET","hydra:operation": "srs","hydra:expects":"", "hydra:returns": "",  "hydra:statusCode": ""},
            {"@id": "http://opengis.org/operations/envelope", "hydra:method": "GET","hydra:operation": "envelope","hydra:expects":"", "hydra:returns": "http://geojson.org/geojson-ld/vocab.html#geometry",  "hydra:statusCode": ""},
        ]
        return arr_dic

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


