from context.context import ContextBase
from context.hydra import HydraClassSerializer

class APIRootHydraSerializer(HydraClassSerializer):

    class_name = "EntryPoint"
    is_collection = True

    def createProperties(self, property_serializer):
        attributes = {
            'unidades federativas': '',
            'municipios': '',
            'outras unidades protegidas': '',
            'outros limites oficiais': '',
            'paises': '',
            'terras indigenas': '',
            'unidades de conservacao nao snuc': '',
            'unidades de protecao integral': '',
            'unidades de uso sustentavel': '',
            'aglomerados rurais de extensao urbana': '',
            'aglomerados rurais isolado': '',
            'aldeias indigenas': '',
            'areas edificadas': '',
            'capitais': '',
            'vilas': '',
            'curvas batimetricas': '',
            #'curvas de nivel': '',
            'dunas': '',
            'elementos fisiografico natural': '',
            'picos': '',
            'pontos cotados altimetricos': '',
            'pontos cotados batimetricos': '',
            'eclusas': '',
            'edificacoes de construcao portuaria': '',
            'edificacoes de construcao aeroportuaria': '',
            'edificacoes de metro ferroviaria': '',
            'fundeadouros': '',
            'pistas de ponto pouso': '',
            'pontes': '',
            'sinalizacoes': '',
            'travessias': '',
            'trechos dutos': '',
            'trechos ferroviarios': '',
            'trechos hidroviarios': '',
            #'trechos rodoviarios': '',
            'tuneis': '',
            'brejos e pantanos': '',
            'mangues': '',
            'vegetacoes de restinga': '',
            'edificacoes publica militar': '',
            'postos fiscais': '',
            'edificacoes agropecuarias de extracao vegetal e pesca': '',
            'edificacoes industrial': '',
            'extracoes minerais': '',
            'edificacoes religiosa': '',
            'estacoes geradoras de energia eletrica': '',
            'hidreletricas': '',
            'termeletricas': '',
            'torres de energia': '',
            'bancos de areia': '',
            'barragens': '',
            'corredeiras': '',
            'fozes maritima': '',
            'ilhas': '',
            'massas dagua': '',
            'quedas dagua': '',
            'recifes': '',
            'rochas em agua': '',
            'sumidouros vertedouros': '',
            'terrenos sujeito a inundacao': '',
            'trechos de drenagem': '',
            'trechos de massa dagua': '',
            'areas de desenvolvimento de controle': '',
            'marcos de limite': '',
            'pontos geodesicos': '',
        }
        for attribute in attributes:
            property_serializer.addProperty(name=attribute, type=property_serializer.getTypeID(), readable=True, writeable=False)

    def createMethods(self, method_serializer):
        method_serializer.addCustomOperation(title="List", returns=method_serializer.getClassName(), view="bcim_v1:api_root")


class APIRootContext(ContextBase):

    operation_class = APIRootHydraSerializer

    def createAttributes(self):
        attributes = {
            'unidades federativas': '',
            'municipios': '',
            'outras unidades protegidas': '',
            'outros limites oficiais': '',
            'paises': '',
            'terras indigenas': '',
            'unidades de conservacao nao snuc': '',
            'unidades de protecao integral': '',
            'unidades de uso sustentavel': '',
            'aglomerados rurais de extensao urbana': '',
            'aglomerados rurais isolado': '',
            'aldeias indigenas': '',
            'areas edificadas': '',
            'capitais': '',
            'vilas': '',
            'curvas batimetricas': '',
            #'curvas de nivel': '',
            'dunas': '',
            'elementos fisiografico natural': '',
            'picos': '',
            'pontos cotados altimetricos': '',
            'pontos cotados batimetricos': '',
            'eclusas': '',
            'edificacoes de construcao portuaria': '',
            'edificacoes de construcao aeroportuaria': '',
            'edificacoes de metro ferroviaria': '',
            'fundeadouros': '',
            'pistas de ponto pouso': '',
            'pontes': '',
            'sinalizacoes': '',
            'travessias': '',
            'trechos dutos': '',
            'trechos ferroviarios': '',
            'trechos hidroviarios': '',
            #'trechos rodoviarios': '',
            'tuneis': '',
            'brejos e pantanos': '',
            'mangues': '',
            'vegetacoes de restinga': '',
            'edificacoes publica militar': '',
            'postos fiscais': '',
            'edificacoes agropecuarias de extracao vegetal e pesca': '',
            'edificacoes industrial': '',
            'extracoes minerais': '',
            'edificacoes religiosa': '',
            'estacoes geradoras de energia eletrica': '',
            'hidreletricas': '',
            'termeletricas': '',
            'torres de energia': '',
            'bancos de areia': '',
            'barragens': '',
            'corredeiras': '',
            'fozes maritima': '',
            'ilhas': '',
            'massas dagua': '',
            'quedas dagua': '',
            'recifes': '',
            'rochas em agua': '',
            'sumidouros vertedouros': '',
            'terrenos sujeito a inundacao': '',
            'trechos de drenagem': '',
            'trechos de massa dagua': '',
            'areas de desenvolvimento de controle': '',
            'marcos de limite': '',
            'pontos geodesicos': '',
        }
        schemaUrl = "http://schema.org/"
        for attribute in attributes:
            self.addAttribute(attribute, id=schemaUrl+attributes[attribute], type="@id")

class UnidadeFederacaoContext(ContextBase):

    def createAttributes(self):
        schemaUrl = "http://schema.org/"

        attributes = {
            'id_objeto': {'id':'', 'type': self.getTypeID()},
            'nome': {'id':'name', 'type': self.getTypeString()},
            'nomeabrev': {'id':'', 'type': self.getTypeString()},
            'geometriaaproximada': {'id':'', 'type': ''},
            'sigla': {'id':'', 'type': self.getTypeString()},
            'geocodigo': {'id':self.getTypeProductID(), 'type': self.getTypeString()},
            'geom': {'id':'', 'type': ''}
        }

        for attribute in attributes:
            attr = attributes[attribute]
            self.addAttribute(attribute, id=schemaUrl+attr["id"], type=attr["type"])

# class UnidadeFederacaoHydraSerializerList(HydraClassSerializer):
#
#     class_name = "EntryPoint"
#     is_collection = True
#
#     def createProperties(self, property_serializer):
#         property_serializer.addProperty(name='id_objeto', type=property_serializer.getTypeInteger(), readable=True)
#         property_serializer.addProperty(name='nome', type=property_serializer.getTypeString(), required=True, readable=True, writeable=True)
#         property_serializer.addProperty(name='nomeabrev', type=property_serializer.getTypeString(), required=True, readable=True, writeable=True)
#         property_serializer.addProperty(name='geometriaaproximada', type=property_serializer.getTypeBoolean(), required=True, readable=True, writeable=True)
#         property_serializer.addProperty(name='sigla', type=property_serializer.getTypeID(), required=True, readable=True, writeable=True)
#         property_serializer.addProperty(name='geocodigo', type=property_serializer.getTypeString(), required=True, readable=True, writeable=True)
#         property_serializer.addProperty(name='geom', type=property_serializer.getTypeID(), readable=True)
#
#     def createMethods(self, method_serializer):
#         method_serializer.addDefaultCreateOperation(view="community:list")
#         method_serializer.addCustomOperation(title="List", returns=method_serializer.getClassNameCollection(), view="community:list")