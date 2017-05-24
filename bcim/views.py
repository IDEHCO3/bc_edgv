from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status

from bcim.contexts import UnidadeFederacaoContext
from bcim.utils import *

from rest_framework import permissions

from rest_framework import generics
from bcim.serializers import *


from context_api.views import *
from hyper_resource.views import *


def get_root_response(request):
    format = None
    root_links = {
        'unidades federativas': reverse('bcim_v1:uf_list', request=request, format=format),
        'municipios': reverse('bcim_v1:municipio_list', request=request, format=format),
        #'outras unidades protegidas': reverse('bcim_v1:outras_unid_protegidas_list', request=request, format=format),
        'outros limites oficiais': reverse('bcim_v1:outros_limites_oficiais_list', request=request, format=format),
        'paises': reverse('bcim_v1:pais_list', request=request, format=format),
        'terras indigenas': reverse('bcim_v1:terra_indigena_list', request=request, format=format),
        'unidades de conservacao nao snuc': reverse('bcim_v1:unidade_conservacao_nao_snuc_list', request=request, format=format),
        'unidades de protecao integral': reverse('bcim_v1:unidade_protecao_integral_list', request=request, format=format),
        'unidades de uso sustentavel': reverse('bcim_v1:unidade_uso_sustentavel_list', request=request, format=format),
        'aglomerados rurais de extensao urbana': reverse('bcim_v1:aglomerado_rural_de_extensao_urbana_list', request=request, format=format),
        'aglomerados rurais isolado': reverse('bcim_v1:aglomerado_rural_isolado_list', request=request, format=format),
        'aldeias indigenas': reverse('bcim_v1:aldeia_indigena_list', request=request, format=format),
        'areas edificadas': reverse('bcim_v1:area_edificada_list', request=request, format=format),
        'capitais': reverse('bcim_v1:capital_list', request=request, format=format),
        'cidades': reverse('bcim_v1:cidade_list', request=request, format=format),
        'vilas': reverse('bcim_v1:vila_list', request=request, format=format),
        'curvas batimetricas': reverse('bcim_v1:curva_batimetrica_list', request=request, format=format),
        #'curvas de nivel': reverse('bcim_v1:curva_nivel_list', request=request, format=format),
        'curvas de nivel': reverse('bcim_v1:curva_nivel_list', request=request, format=format),
        'dunas': reverse('bcim_v1:duna_list', request=request, format=format),
        'elementos fisiografico natural': reverse('bcim_v1:elemento_fisiografico_natural_list', request=request, format=format),
        'picos': reverse('bcim_v1:pico_list', request=request, format=format),
        'pontos cotados altimetricos': reverse('bcim_v1:ponto_cotado_altimetrico_list', request=request, format=format),
        'pontos cotados batimetricos': reverse('bcim_v1:ponto_cotado_batimetrico_list', request=request, format=format),
        'eclusas': reverse('bcim_v1:eclusa_list', request=request, format=format),
        'edificacoes de construcao portuaria': reverse('bcim_v1:edif_const_portuaria_list', request=request, format=format),
        'edificacoes de construcao aeroportuaria': reverse('bcim_v1:edif_const_aeroportuaria_list', request=request, format=format),
        'edificacoes de metro ferroviaria': reverse('bcim_v1:edif_metro_ferroviaria_list', request=request, format=format),
        'fundeadouros': reverse('bcim_v1:fundeadouro_list', request=request, format=format),
        'pistas de ponto pouso': reverse('bcim_v1:pista_ponto_pouso_list', request=request, format=format),
        'pontes': reverse('bcim_v1:ponte_list', request=request, format=format),
        'sinalizacoes': reverse('bcim_v1:sinalizacao_list', request=request, format=format),
        'travessias': reverse('bcim_v1:travessia_list', request=request, format=format),
        'trechos dutos': reverse('bcim_v1:trecho_duto_list', request=request, format=format),
        'trechos ferroviarios': reverse('bcim_v1:trecho_ferroviario_list', request=request, format=format),
        'trechos hidroviarios': reverse('bcim_v1:trecho_hidroviario_list', request=request, format=format),
        #'trechos rodoviarios': reverse('bcim_v1:trecho_rodoviario_list', request=request, format=format),
        'trechos rodoviarios': reverse('bcim_v1:trecho_rodoviario_list', request=request, format=format),
        'tuneis': reverse('bcim_v1:tunel_list', request=request, format=format),
        'brejos e pantanos': reverse('bcim_v1:brejo_pantano_list', request=request, format=format),
        'mangues': reverse('bcim_v1:mangue_list', request=request, format=format),
        'vegetacoes de restinga': reverse('bcim_v1:veg_restinga_list', request=request, format=format),
        'edificacoes publica militar': reverse('bcim_v1:edif_pub_militar_list', request=request, format=format),
        'postos fiscais': reverse('bcim_v1:posto_fiscal_list', request=request, format=format),
        'edificacoes agropecuarias de extracao vegetal e pesca': reverse('bcim_v1:edif_agropec_ext_vegetal_pesca_list', request=request, format=format),
        'edificacoes industrial': reverse('bcim_v1:edif_industrial_list', request=request, format=format),
        'extracoes minerais': reverse('bcim_v1:ext_mineral_list', request=request, format=format),
        'edificacoes religiosa': reverse('bcim_v1:edif_religiosa_list', request=request, format=format),
        'estacoes geradoras de energia eletrica': reverse('bcim_v1:est_gerad_energia_eletrica_list', request=request, format=format),
        'hidreletricas': reverse('bcim_v1:hidreletrica_list', request=request, format=format),
        'termeletricas': reverse('bcim_v1:termeletrica_list', request=request, format=format),
        'torres de energia': reverse('bcim_v1:torre_energia_list', request=request, format=format),
        'bancos de areia': reverse('bcim_v1:banco_areia_list', request=request, format=format),
        'barragens': reverse('bcim_v1:barragem_list', request=request, format=format),
        'corredeiras': reverse('bcim_v1:corredeira_list', request=request, format=format),
        'fozes maritima': reverse('bcim_v1:foz_maritima_list', request=request, format=format),
        'ilhas': reverse('bcim_v1:ilha_list', request=request, format=format),
        'massas dagua': reverse('bcim_v1:massa_dagua_list', request=request, format=format),
        'quedas dagua': reverse('bcim_v1:queda_dagua_list', request=request, format=format),
        'recifes': reverse('bcim_v1:recife_list', request=request, format=format),
        'rochas em agua': reverse('bcim_v1:rocha_em_agua_list', request=request, format=format),
        'sumidouros vertedouros': reverse('bcim_v1:sumidouro_vertedouro_list', request=request, format=format),
        'terrenos sujeito a inundacao': reverse('bcim_v1:terreno_sujeito_inundacao_list', request=request, format=format),
        'trechos de drenagem': reverse('bcim_v1:trecho_drenagem_list', request=request, format=format),
        'trechos de massa dagua': reverse('bcim_v1:trecho_massa_dagua_list', request=request, format=format),
        'areas de desenvolvimento de controle': reverse('bcim_v1:area_desenvolvimento_controle_list', request=request, format=format),
        'marcos de limite': reverse('bcim_v1:marco_de_limite_list', request=request, format=format),
        #'pontos geodesicos': reverse('bcim_v1:ponto_exibicao_wgs84_list', request=request, format=format),
    }

    for key in serializers_dict:
        name = serializers_dict[key].get('name')
        root_links[name] = reverse('bcim_v1:general_list', request=request, format=format, kwargs={'model_class': key})

    ordered_dict_of_link = OrderedDict(sorted(root_links.items(), key=lambda t: t[0]))
    return ordered_dict_of_link

class APIRoot(APIView):

    def __init__(self):
        super(APIRoot, self).__init__()
        self.base_context = BaseContext('api-root')

    def add_url_in_header(self, url, response, rel):
        link = ' <'+url+'>; rel=\"'+rel+'\" '
        if "Link" not in response:
            response['Link'] = link
        else:
            response['Link'] += "," + link
        return response

    def options(self, request, *args, **kwargs):
        context = self.base_context.getContextData(request)
        root_links = get_root_response(request)
        context.update(root_links)
        response = Response(context, status=status.HTTP_200_OK, content_type="application/ld+json")
        entry_pointURL = reverse('bcim_v1:api_root', request=request)
        response = self.add_url_in_header(entry_pointURL, response, 'http://schema.org/EntryPoint')
        response = self.base_context.addContext(request, response)
        return response

    def get(self, request, *args, **kwargs):
        root_links = get_root_response(request)
        response = Response(root_links)
        entry_pointURL = reverse('bcim_v1:api_root', request=request)
        response = self.add_url_in_header(entry_pointURL, response, 'http://schema.org/EntryPoint')
        return self.base_context.addContext(request, response)


class UnidadeFederacaoDetail(FeatureResource):

    serializer_class = UnidadeFederacaoSerializer
    contextclassname = 'unidades-federativas'

<<<<<<< HEAD
    def initialize_context(self):
        self.context_resource = UnidadeFederacaoContext()
=======
    def get(self, request, *args, **kwargs):
        if kwargs.get('sigla') is not None:
            kwargs['sigla'] = kwargs.get('sigla').upper()
        return super(UnidadeFederacaoDetail, self).get(request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        if kwargs.get('sigla') is not None:
            kwargs['sigla'] = kwargs.get('sigla').upper()
        return super(UnidadeFederacaoDetail, self).options(request, *args, **kwargs)
>>>>>>> 9332252eef8f298a323920d43ed1dfc459a14860

class UnidadeFederacaoList(HandleFunctionsList):

    queryset = UnidadeFederacao.objects.all()
    serializer_class = UnidadeFederacaoSerializer
    contextclassname = 'unidades-federativas'
    iri_metadata = 'http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&id=ff2d4215-9843-4137-bad9-c15f2a8caa9e'
    iri_style = 'http://styles.idehco4.tk/styles/unidade_federacao.sld'

    def get_queryset(self):

        geocodigo_uf = self.kwargs.get("geocodigo")
        if geocodigo_uf is not None:
            return self.queryset.filter(geocodigo=geocodigo_uf)

        sigla_uf = self.kwargs.get("sigla")
        if sigla_uf is not None:
            return self.queryset.filter(sigla=sigla_uf.upper())

        siglas = self.kwargs.get("siglas")
        if siglas is not None:
            return self.queryset.filter(sigla__in=siglas.split(","))

        return super(UnidadeFederacaoList, self).get_queryset()

class MunicipioList(HandleFunctionsList):

    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    contextclassname = 'municipios'
    iri_metadata = 'http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&id=3cd8176c-2f59-4eab-8232-3da978d0ecf3'
    iri_style = 'http://styles.idehco4.tk/styles/municipio.sld'

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'

class MunicipioFiltered(HandleFunctionsList):

    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    contextclassname = 'municipios'

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        nome_municipio = self.kwargs.get("nome")

        #sigla_uf = self.request.query_params.get('sigla', None)

        if nome_municipio is not None:

            return self.queryset.filter(nome=nome_municipio)


        return self.queryset

class MunicipioDetail(HandleFunctionDetail):

    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    contextclassname = 'municipios'
    lookup_field = "geocodigo"


class OutrasUnidProtegidasList(HandleFunctionsList):

    queryset = OutrasUnidProtegidas.objects.all()
    serializer_class = OutrasUnidProtegidasSerializer
    contextclassname = 'outras-unidades-protegidas'

class OutrasUnidProtegidasDetail(HandleFunctionDetail):

    serializer_class = OutrasUnidProtegidasSerializer
    contextclassname = 'outras-unidades-protegidas'

class OutrosLimitesOficiaisList(HandleFunctionsList):

    queryset = OutrosLimitesOficiais.objects.all()
    serializer_class = OutrosLimitesOficiaisSerializer
    contextclassname = 'outros-limites-oficiais'

class OutrosLimitesOficiaisDetail(HandleFunctionDetail):

    serializer_class = OutrosLimitesOficiaisSerializer
    contextclassname = 'outros-limites-oficiais'

class PaisList(HandleFunctionsList):

    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    contextclassname = 'paises'

class PaisDetail(HandleFunctionDetail):

    serializer_class = PaisSerializer
    contextclassname = 'paises'

class TerraIndigenaList(HandleFunctionsList):

    queryset = TerraIndigena.objects.all()
    serializer_class = TerraIndigenaSerializer
    contextclassname = 'terras-indigenas'

class TerraIndigenaDetail(HandleFunctionDetail):
    serializer_class = TerraIndigenaSerializer
    contextclassname = 'terras-indigenas'

class UnidadeConservacaoNaoSnucList(HandleFunctionsList):

    queryset = UnidadeConservacaoNaoSnuc.objects.all()
    serializer_class = UnidadeConservacaoNaoSnucSerializer
    contextclassname = 'unidades-de-conservacao-nao-snuc'

class UnidadeConservacaoNaoSnucDetail(HandleFunctionDetail):

    serializer_class = UnidadeConservacaoNaoSnucSerializer
    contextclassname = 'unidades-de-conservacao-nao-snuc'

class UnidadeProtecaoIntegralList(HandleFunctionsList):

    queryset = UnidadeProtecaoIntegral.objects.all()
    serializer_class = UnidadeProtecaoIntegralSerializer
    contextclassname = 'unidades-de-protecao-integral'

class UnidadeProtecaoIntegralDetail(HandleFunctionDetail):

    serializer_class = UnidadeProtecaoIntegralSerializer
    contextclassname = 'unidades-de-protecao-integral'

class UnidadeUsoSustentavelList(HandleFunctionsList):

    queryset = UnidadeUsoSustentavel.objects.all()
    serializer_class = UnidadeUsoSustentavelSerializer
    contextclassname = 'unidades-de-uso-sustentavel'

class UnidadeUsoSustentavelDetail(HandleFunctionDetail):

    serializer_class = UnidadeUsoSustentavelSerializer
    contextclassname = 'unidades-de-uso-sustentavel'

class AglomeradoRuralDeExtensaoUrbanaList(HandleFunctionsList):

    queryset = AglomeradoRuralDeExtensaoUrbana.objects.all()
    serializer_class = AglomeradoRuralDeExtensaoUrbanaSerializer
    contextclassname = 'aglomerados-rurais-de-extensao-urbana'

class AglomeradoRuralDeExtensaoUrbanaDetail(HandleFunctionDetail):

    serializer_class = AglomeradoRuralDeExtensaoUrbanaSerializer
    contextclassname = 'aglomerados-rurais-de-extensao-urbana'

class AglomeradoRuralIsoladoList(HandleFunctionsList):

    queryset = AglomeradoRuralIsolado.objects.all()
    serializer_class = AglomeradoRuralIsoladoSerializer
    contextclassname = 'aglomerados-rurais-isolado'

class AglomeradoRuralIsoladoDetail(HandleFunctionDetail):

    serializer_class = AglomeradoRuralIsoladoSerializer
    contextclassname = 'aglomerados-rurais-isolado'

class AldeiaIndigenaList(HandleFunctionsList):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer
    contextclassname = 'aldeias-indigenas'

class AldeiaIndigenaListFiltered(HandleFunctionsList):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer
    contextclassname = 'aldeias-indigenas'

class AldeiaIndigenaListFilteredByQueryParameters(HandleFunctionsList):

    serializer_class = AldeiaIndigenaSerializer
    contextclassname = 'aldeias-indigenas'

class AldeiaIndigenaDetail(HandleFunctionDetail):

    serializer_class = AldeiaIndigenaSerializer
    contextclassname = 'aldeias-indigenas'

class AreaEdificadaList(HandleFunctionsList):

    queryset = AreaEdificada.objects.all()
    serializer_class = AreaEdificadaSerializer
    contextclassname = 'areas-edificadas'

class AreaEdificadaDetail(HandleFunctionDetail):

    serializer_class = AreaEdificadaSerializer
    contextclassname = 'areas-edificadas'

class CapitalList(HandleFunctionsList):

    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    contextclassname = 'capitais'


class CapitalDetail(HandleFunctionDetail):

    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    contextclassname = 'capitais'

class CidadeList(HandleFunctionsList):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    contextclassname = 'cidades'

class CidadeDetail(HandleFunctionDetail):

    serializer_class = CidadeSerializer
    contextclassname = 'cidades'

class VilaList(HandleFunctionsList):

    queryset = Vila.objects.all()
    serializer_class = VilaSerializer
    contextclassname = 'vilas'

class VilaDetail(HandleFunctionDetail):

    serializer_class = VilaSerializer
    contextclassname = 'vilas'

class CurvaBatimetricaList(HandleFunctionsList):

    queryset = CurvaBatimetrica.objects.all()
    serializer_class = CurvaBatimetricaSerializer
    contextclassname = 'curvas-batimetricas'

class CurvaBatimetricaDetail(HandleFunctionDetail):

    serializer_class = CurvaBatimetricaSerializer
    contextclassname = 'curvas-batimetricas'

class CurvaNivelList(HandleFunctionsList):

    queryset = CurvaNivel.objects.all()
    serializer_class = CurvaNivelSerializer
    contextclassname ='curvas-de-nivel'

class CurvaNivelDetail(HandleFunctionDetail):

    serializer_class = CurvaNivelSerializer
    contextclassname = 'curvas-de-nivel'

class DunaList(HandleFunctionsList):

    queryset = Duna.objects.all()
    serializer_class = DunaSerializer
    contextclassname = 'dunas'

class DunaDetail(HandleFunctionDetail):

    serializer_class = DunaSerializer
    contextclassname = 'dunas'

class ElementoFisiograficoNaturalList(HandleFunctionsList):

    queryset = ElementoFisiograficoNatural.objects.all()
    serializer_class = ElementoFisiograficoNaturalSerializer
    contextclassname = 'elementos-fisiografico-natural'

class ElementoFisiograficoNaturalDetail(HandleFunctionDetail):

    serializer_class = ElementoFisiograficoNaturalSerializer
    contextclassname = 'elementos-fisiografico-natural'

class PicoList(HandleFunctionsList):

    queryset = Pico.objects.all()
    serializer_class = PicoSerializer
    contextclassname = 'picos'

class PicoDetail(HandleFunctionDetail):

    serializer_class = PicoSerializer
    contextclassname = 'picos'

class PontoCotadoAltimetricoList(HandleFunctionsList):

    queryset = PontoCotadoAltimetrico.objects.all()
    serializer_class = PontoCotadoAltimetricoSerializer
    contextclassname = 'pontos-cotados-altimetricos'

class PontoCotadoAltimetricoDetail(HandleFunctionDetail):

    serializer_class = PontoCotadoAltimetricoSerializer
    contextclassname = 'pontos-cotados-altimetricos'

class PontoCotadoBatimetricoList(HandleFunctionsList):

    queryset = PontoCotadoBatimetrico.objects.all()
    serializer_class = PontoCotadoBatimetricoSerializer
    contextclassname = 'pontos-cotados-batimetricos'

class PontoCotadoBatimetricoDetail(HandleFunctionDetail):

    serializer_class = PontoCotadoBatimetricoSerializer
    contextclassname = 'pontos-cotados-batimetricos'

class EclusaList(HandleFunctionsList):

    queryset = Eclusa.objects.all()
    serializer_class = EclusaSerializer
    contextclassname = 'eclusas'

class EclusaDetail(HandleFunctionDetail):

    serializer_class = EclusaSerializer
    contextclassname = 'eclusas'

class EdifConstPortuariaList(HandleFunctionsList):

    queryset = EdifConstPortuaria.objects.all()
    serializer_class = EdifConstPortuariaSerializer
    contextclassname = 'edificacoes-de-construcao-portuaria'

class EdifConstPortuariaDetail(HandleFunctionDetail):

    serializer_class = EdifConstPortuariaSerializer
    contextclassname = 'edificacoes-de-construcao-portuaria'

class EdifConstrAeroportuariaList(HandleFunctionsList):

    queryset = EdifConstrAeroportuaria.objects.all()
    serializer_class = EdifConstrAeroportuariaSerializer
    contextclassname = 'edificacoes-de-construcao-aeroportuaria'

class EdifConstrAeroportuariaDetail(HandleFunctionDetail):

    serializer_class = EdifConstPortuariaSerializer
    contextclassname = 'edificacoes-de-construcao-aeroportuaria'

class EdifMetroFerroviariaList(HandleFunctionsList):

    queryset = EdifMetroFerroviaria.objects.all()
    serializer_class = EdifMetroFerroviariaSerializer
    contextclassname = 'edificacoes-metro-ferroviaria'

class EdifMetroFerroviariaDetail(HandleFunctionDetail):

    serializer_class = EdifMetroFerroviariaSerializer
    contextclassname = 'edificacoes-metro-ferroviaria'

class FundeadouroList(HandleFunctionsList):

    queryset = Fundeadouro.objects.all()
    serializer_class = FundeadouroSerializer
    contextclassname = 'fundeadouros'

class FundeadouroDetail(HandleFunctionDetail):

    serializer_class = FundeadouroSerializer
    contextclassname = 'fundeadouros'

class PistaPontoPousoList(HandleFunctionsList):

    queryset = PistaPontoPouso.objects.all()
    serializer_class = PistaPontoPousoSerializer
    contextclassname = 'pistas-de-ponto-pouso'

class PistaPontoPousoDetail(HandleFunctionDetail):

    serializer_class = PistaPontoPousoSerializer
    contextclassname = 'pistas-de-ponto-pouso'

class PonteList(HandleFunctionsList):

    queryset = Ponte.objects.all()
    serializer_class = PonteSerializer
    contextclassname = 'pontes'

class PonteDetail(HandleFunctionDetail):

    serializer_class = PonteSerializer
    contextclassname = 'pontes'

class SinalizacaoList(HandleFunctionsList):

    queryset = Sinalizacao.objects.all()
    serializer_class = SinalizacaoSerializer
    contextclassname = 'sinalizacaoes'

class SinalizacaoDetail(HandleFunctionDetail):

    serializer_class = SinalizacaoSerializer
    contextclassname = 'sinalizacaoes'

class TravessiaList(HandleFunctionsList):

    queryset = Travessia.objects.all()
    serializer_class = TravessiaSerializer
    contextclassname = 'travessias'

class TravessiaDetail(HandleFunctionDetail):

    serializer_class = TravessiaSerializer
    contextclassname = 'travessias'

class TrechoDutoList(HandleFunctionsList):

    queryset = TrechoDuto.objects.all()
    serializer_class = TrechoDutoSerializer
    contextclassname = 'trechos-dutos'

class TrechoDutoDetail(HandleFunctionDetail):

    serializer_class = TrechoDutoSerializer
    contextclassname = 'trechos-dutos'

class TrechoFerroviarioList(HandleFunctionsList):

    queryset = TrechoFerroviario.objects.all()
    serializer_class = TrechoFerroviarioSerializer
    contextclassname = 'trechos-ferroviarios'

class TrechoFerroviarioDetail(HandleFunctionDetail):

    serializer_class = TrechoFerroviarioSerializer
    contextclassname = 'trechos-ferroviarios'

class TrechoHidroviarioList(HandleFunctionsList):

    queryset = TrechoHidroviario.objects.all()
    serializer_class = TrechoHidroviarioSerializer
    contextclassname = 'trechos-hidroviarios'

class TrechoHidroviarioDetail(HandleFunctionDetail):

    serializer_class = TrechoHidroviarioSerializer
    contextclassname = 'trechos-hidroviarios'

class TrechoRodoviarioList(HandleFunctionsList):

    queryset = TrechoRodoviario.objects.all()
    serializer_class = TrechoRodoviarioSerializer
    contextclassname = 'trechos-rodoviarios'

class TrechoRodoviarioDetail(HandleFunctionDetail):

    serializer_class = TrechoRodoviarioSerializer
    contextclassname = 'trechos-rodoviarios'

class TunelList(HandleFunctionsList):

    queryset = Tunel.objects.all()
    serializer_class = TunelSerializer
    contextclassname = 'tuneis'

class TunelDetail(HandleFunctionDetail):

    serializer_class = TunelSerializer
    contextclassname = 'tuneis'

class BrejoPantanoList(HandleFunctionsList):

    queryset = BrejoPantano.objects.all()
    serializer_class = BrejoPantanoSerializer
    contextclassname = 'brejos-e-pantanos'

class BrejoPantanoDetail(HandleFunctionDetail):

    serializer_class = BrejoPantanoSerializer
    contextclassname = 'brejos-e-pantanos'

class MangueList(HandleFunctionsList):

    queryset = Mangue.objects.all()
    serializer_class = MangueSerializer
    contextclassname = 'mangues'

class MangueDetail(HandleFunctionDetail):

    serializer_class = MangueSerializer
    contextclassname  = 'mangues'

class VegRestingaList(HandleFunctionsList):

    queryset = VegRestinga.objects.all()
    serializer_class = VegRestingaSerializer
    contextclassname = 'vegetacoes-de-restinga'

class VegRestingaDetail(HandleFunctionDetail):

    serializer_class = VegRestingaSerializer
    contextclassname = 'vegetacoes-de-restinga'

class EdifPubMilitarList(HandleFunctionsList):

    queryset = EdifPubMilitar.objects.all()
    serializer_class = EdifPubMilitarSerializer
    contextclassname = 'edificacoes-publica-militar'

class EdifPubMilitarDetail(HandleFunctionDetail):

    serializer_class = EdifPubMilitarSerializer
    contextclassname = 'edificacoes-publica-militar'

class PostoFiscalList(HandleFunctionsList):

    queryset = PostoFiscal.objects.all()
    serializer_class = PostoFiscalSerializer
    contextclassname = 'postos-fiscais'


class PostoFiscalDetail(HandleFunctionDetail):

    serializer_class = PostoFiscalSerializer
    contextclassname = 'postos-fiscais'

class EdifAgropecExtVegetalPescaList(HandleFunctionsList):

    queryset = EdifAgropecExtVegetalPesca.objects.all()
    serializer_class = EdifAgropecExtVegetalPescaSerializer
    contextclassname = 'edificacoes-agropecuarias-de-extracao-vegetal-e-pesca'

class EdifAgropecExtVegetalPescaDetail(HandleFunctionDetail):

    serializer_class = EdifAgropecExtVegetalPescaSerializer
    contextclassname = 'edificacoes-agropecuarias-de-extracao-vegetal-e-pesca'

class EdifIndustrialList(HandleFunctionsList):

    queryset = EdifIndustrial.objects.all()
    serializer_class = EdifIndustrialSerializer
    contextclassname = 'edificacoes-industrial'

class EdifIndustrialDetail(HandleFunctionDetail):

    serializer_class = EdifIndustrialSerializer
    contextclassname = 'edificacoes-industrial'

class ExtMineralList(HandleFunctionsList):

    queryset = ExtMineral.objects.all()
    serializer_class = ExtMineralSerializer
    contextclassname = 'extracoes-minerais'

class ExtMineralDetail(HandleFunctionDetail):

    serializer_class = ExtMineralSerializer
    contextclassname = 'extracoes-minerais'

class EdifReligiosaList(HandleFunctionsList):

    queryset = EdifReligiosa.objects.all()
    serializer_class = EdifReligiosaSerializer
    contextclassname = 'edificacoes-religiosa'

class EdifReligiosaDetail(HandleFunctionDetail):

    serializer_class = EdifReligiosaSerializer
    contextclassname = 'edificacoes-religiosa'

class EstGeradEnergiaEletricaList(HandleFunctionsList):

    queryset = EstGeradEnergiaEletrica.objects.all()
    serializer_class = EstGeradEnergiaEletricaSerializer
    contextclassname = 'estacoes-geradoras-de-energia-eletrica'

class EstGeradEnergiaEletricaDetail(HandleFunctionDetail):

    serializer_class = EstGeradEnergiaEletricaSerializer
    contextclassname = 'estacoes-geradoras-de-energia-eletrica'

class HidreletricaList(HandleFunctionsList):

    queryset = Hidreletrica.objects.all()
    serializer_class = HidreletricaSerializer
    contextclassname = 'hidreletricas'

class HidreletricaDetail(HandleFunctionDetail):

    serializer_class = HidreletricaSerializer
    contextclassname = 'hidreletricas'

class TermeletricaList(HandleFunctionsList):

    queryset = Termeletrica.objects.all()
    serializer_class = TermeletricaSerializer
    contextclassname = 'termeletricas'

class TermeletricaDetail(HandleFunctionDetail):

    serializer_class = TermeletricaSerializer
    contextclassname = 'termeletricas'

class TorreEnergiaList(HandleFunctionsList):

    queryset = TorreEnergia.objects.all()
    serializer_class = TorreEnergiaSerializer
    contextclassname = 'torres-de-energia'

class TorreEnergiaDetail(HandleFunctionDetail):

    serializer_class = TorreEnergiaSerializer
    contextclassname = 'torres-de-energia'

class BancoAreiaList(HandleFunctionsList):

    queryset = BancoAreia.objects.all()
    serializer_class = BancoAreiaSerializer
    contextclassname = 'bancos-de-areia'

class BancoAreiaDetail(HandleFunctionDetail):

    serializer_class = BancoAreiaSerializer
    contextclassname = 'bancos-de-areia'

class BarragemList(HandleFunctionsList):

    queryset = Barragem.objects.all()
    serializer_class = BarragemSerializer
    contextclassname = 'barragens'

class BarragemDetail(HandleFunctionDetail):

    serializer_class = BarragemSerializer
    contextclassname = 'barragens'

class CorredeiraList(HandleFunctionsList):

    queryset = Corredeira.objects.all()
    serializer_class = CorredeiraSerializer
    contextclassname = 'corredeiras'

class CorredeiraDetail(HandleFunctionDetail):

    serializer_class = CorredeiraSerializer
    contextclassname = 'corredeiras'

class FozMaritimaList(HandleFunctionsList):

    queryset = FozMaritima.objects.all()
    serializer_class = FozMaritimaSerializer
    contextclassname = 'fozes-maritima'

class FozMaritimaDetail(HandleFunctionDetail):

    serializer_class = FozMaritimaSerializer
    contextclassname = 'fozes-maritima'

class IlhaList(HandleFunctionsList):

    queryset = Ilha.objects.all()
    serializer_class = IlhaSerializer
    contextclassname = 'ilhas'

class IlhaDetail(HandleFunctionDetail):

    serializer_class = IlhaSerializer
    contextclassname = 'ilhas'

class MassaDaguaList(HandleFunctionsList):

    queryset = MassaDagua.objects.all()
    serializer_class = MassaDaguaSerializer
    contextclassname = 'massas-dagua'

class MassaDaguaDetail(HandleFunctionDetail):

    serializer_class = MassaDaguaSerializer
    contextclassname = 'massas-dagua'

class QuedaDaguaList(HandleFunctionsList):

    queryset = QuedaDagua.objects.all()
    serializer_class = QuedaDaguaSerializer
    contextclassname = 'quedas-dagua'

class QuedaDaguaDetail(HandleFunctionDetail):

    serializer_class = QuedaDaguaSerializer
    contextclassname = 'quedas-dagua'

class RecifeList(HandleFunctionsList):

    #queryset = Recife.objects.all()
    serializer_class = RecifeSerializer
    contextclassname = 'recifes'

class RecifeDetail(HandleFunctionDetail):

    serializer_class = RecifeSerializer
    contextclassname = 'recifes'

class RochaEmAguaList(HandleFunctionsList):

    queryset = RochaEmAgua.objects.all()
    serializer_class = RochaEmAguaSerializer
    contextclassname = 'rochas-em-agua'

class RochaEmAguaDetail(HandleFunctionDetail):

    serializer_class = RochaEmAguaSerializer
    contextclassname = 'rochas-em-agua'

class SumidouroVertedouroList(HandleFunctionsList):

    queryset = SumidouroVertedouro.objects.all()
    serializer_class = SumidouroVertedouroSerializer
    contextclassname = 'sumidouros-vertedouros'

class SumidouroVertedouroDetail(HandleFunctionDetail):

    serializer_class = SumidouroVertedouroSerializer
    contextclassname = 'sumidouros-vertedouros'

class TerrenoSujeitoInundacaoList(HandleFunctionsList):

    queryset = TerrenoSujeitoInundacao.objects.all()
    serializer_class = TerrenoSujeitoInundacaoSerializer
    contextclassname = 'terrenos-sujeito-a-inundacao'

class TerrenoSujeitoInundacaoDetail(HandleFunctionDetail):

    serializer_class = TerrenoSujeitoInundacaoSerializer
    contextclassname = 'terrenos-sujeito-a-inundacao'

class TrechoDrenagemList(HandleFunctionsList):

    queryset = TrechoDrenagem.objects.all()
    serializer_class = TrechoDrenagemSerializer
    contextclassname = 'trechos-de-drenagem'

class TrechoDrenagemDetail(HandleFunctionDetail):

    serializer_class = TrechoDrenagemSerializer
    contextclassname = 'trechos-de-drenagem'

class TrechoMassaDaguaList(HandleFunctionsList):

    queryset = TrechoMassaDagua.objects.all()
    serializer_class = TrechoMassaDaguaSerializer
    contextclassname = 'trechos-de-drenagem'

class TrechoMassaDaguaDetail(HandleFunctionDetail):

    serializer_class = TrechoMassaDaguaSerializer
    contextclassname = 'trechos-de-massa-dagua'

class AreaDesenvolvimentoControleList(HandleFunctionsList):

    queryset = AreaDesenvolvimentoControle.objects.all()
    serializer_class = AreaDesenvolvimentoControleSerializer
    contextclassname = 'areas-de-desenvolvimento-de-controle'

class AreaDesenvolvimentoControleDetail(HandleFunctionDetail):

    serializer_class = AreaDesenvolvimentoControleSerializer
    contextclassname = 'areas-de-desenvolvimento-de-controle'

class MarcoDeLimiteList(HandleFunctionsList):

    queryset = MarcoDeLimite.objects.all()
    serializer_class = MarcoDeLimiteSerializer
    contextclassname = 'marcos-de-limite'

class MarcoDeLimiteDetail(HandleFunctionDetail):

    serializer_class = MarcoDeLimiteSerializer
    contextclassname = 'marcos-de-limite'

