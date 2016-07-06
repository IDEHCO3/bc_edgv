
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from bcim.utils import APIViewDetailSpatialFunction, DefaultsMixin, ResourceListCreateFilteredByQueryParameters, \
    BasicListFiltered, APIViewHypermedia
from .models import UnidadeFederacao,Municipio, OutrasUnidProtegidas, OutrosLimitesOficiais, Pais, TerraIndigena, \
    UnidadeConservacaoNaoSnuc, UnidadeProtecaoIntegral,UnidadeUsoSustentavel, AglomeradoRuralDeExtensaoUrbana, \
    AglomeradoRuralDeExtensaoUrbana, AglomeradoRuralIsolado, AldeiaIndigena, AreaEdificada, Capital, Cidade, Vila, \
    CurvaBatimetrica, CurvaNivel, Duna, ElementoFisiograficoNatural, Pico, PontoCotadoAltimetrico, PontoCotadoBatimetrico, \
    Eclusa, EdifConstPortuaria, EdifConstrAeroportuaria, EdifMetroFerroviaria, Fundeadouro, PistaPontoPouso, Ponte, \
    Sinalizacao, Travessia, TrechoDuto, TrechoFerroviario, TrechoHidroviario, TrechoRodoviario, Tunel, BrejoPantano, \
    Mangue, VegRestinga, EdifPubMilitar, PostoFiscal, EdifAgropecExtVegetalPesca, EdifIndustrial, ExtMineral, EdifReligiosa, \
    EstGeradEnergiaEletrica, Hidreletrica, Termeletrica, TorreEnergia, BancoAreia, Barragem, Corredeira, FozMaritima, \
    Ilha, MassaDagua, QuedaDagua, Recife, RochaEmAgua, SumidouroVertedouro, TerrenoSujeitoInundacao, TrechoDrenagem, \
    TrechoMassaDagua, AreaDesenvolvimentoControle, MarcoDeLimite, PontosExibicaoWgs84


#from permissions import IsOwnerOrReadOnly
from rest_framework import permissions

from rest_framework import generics
from bcim.serializers import UnidadeFederacaoSerializer,MunicipioSerializer, OutrasUnidProtegidasSerializer, \
    OutrosLimitesOficiaisSerializer, PaisSerializer, TerraIndigenaSerializer, UnidadeConservacaoNaoSnucSerializer, \
    UnidadeProtecaoIntegralSerializer, UnidadeUsoSustentavelSerializer, AglomeradoRuralDeExtensaoUrbanaSerializer, \
    AglomeradoRuralIsoladoSerializer, AldeiaIndigenaSerializer, AreaEdificadaSerializer, CapitalSerializer, \
    CidadeSerializer, VilaSerializer, CurvaBatimetricaSerializer, CurvaNivelSerializer, DunaSerializer, \
    ElementoFisiograficoNaturalSerializer, PicoSerializer, PontoCotadoAltimetricoSerializer, PontoCotadoBatimetricoSerializer, \
    EclusaSerializer, EdifConstPortuariaSerializer, EdifConstrAeroportuariaSerializer, EdifMetroFerroviariaSerializer, \
    FundeadouroSerializer, PistaPontoPousoSerializer, PonteSerializer, SinalizacaoSerializer, TravessiaSerializer, \
    TrechoDutoSerializer, TrechoFerroviarioSerializer, TrechoHidroviarioSerializer, TrechoRodoviarioSerializer,\
    TunelSerializer, BrejoPantanoSerializer, MangueSerializer, VegRestingaSerializer, EdifPubMilitarSerializer, \
    PostoFiscalSerializer, EdifAgropecExtVegetalPescaSerializer, EdifIndustrialSerializer, ExtMineralSerializer,\
    EdifReligiosaSerializer, EstGeradEnergiaEletricaSerializer,HidreletricaSerializer, TermeletricaSerializer, \
    TorreEnergiaSerializer, BancoAreiaSerializer, BarragemSerializer, CorredeiraSerializer, FozMaritimaSerializer, \
    IlhaSerializer, MassaDaguaSerializer, QuedaDaguaSerializer, RecifeSerializer, RochaEmAguaSerializer, \
    SumidouroVertedouroSerializer, TerrenoSujeitoInundacaoSerializer, TrechoDrenagemSerializer, TrechoMassaDaguaSerializer, \
    AreaDesenvolvimentoControleSerializer, MarcoDeLimiteSerializer, PontosExibicaoWgs84Serializer


from context.utilities import *
from context.views import CreatorContext

class APIRoot(APIView):

    def options(self, request, *args, **kwargs):
        response = Response(getContextData('api-root', request), status=status.HTTP_200_OK, content_type="application/ld+json")
        response = createLinkOfContext('api-root', request, response)
        return response

    def get(self, request, *args, **kwargs):
        format = None
        response = Response({
            'unidades federativas': reverse('bcim_v1:uf_list', request=request, format=format),
            'municipios': reverse('bcim_v1:municipio_list', request=request, format=format),
            'outras unidades protegidas': reverse('bcim_v1:outras_unid_protegidas_list', request=request, format=format),
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
            'vilas': reverse('bcim_v1:vila_list', request=request, format=format),
            'curvas batimetricas': reverse('bcim_v1:curva_batimetrica_list', request=request, format=format),
            #'curvas de nivel': reverse('bcim_v1:curva_nivel_list', request=request, format=format),
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
            'pontos geodesicos': reverse('bcim_v1:ponto_exibicao_wgs84_list', request=request, format=format),
        })
        response = createLinkOfContext('api-root', request, response)
        return response


class UnidadeFederacaoDetail(APIViewHypermedia):
    """
    Retrieve, update or delete a unidades da federacao instance.
    """
    serializer_class = UnidadeFederacaoSerializer

class UnidadeFederacaoListFilteredByQueryParameters(DefaultsMixin, ResourceListCreateFilteredByQueryParameters):
    """API endpoint for listing and creating sprints."""
    serializer_class = UnidadeFederacaoSerializer

    def options(self, request, *args, **kwargs):
        response = Response(getContextData('unidades-federativas', request), status=status.HTTP_200_OK, content_type="application/ld+json")
        response = createLinkOfContext('unidades-federativas', request, response)
        return response

    def get(self, request, *args, **kwargs):
        response = super(UnidadeFederacaoListFilteredByQueryParameters, self).get(request, *args, **kwargs)
        response = createLinkOfContext('unidades-federativas', request, response)
        return response

class UnidadeFederacaoFiltered(BasicListFiltered):

    queryset = UnidadeFederacao.objects.all()
    serializer_class = UnidadeFederacaoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def get_queryset(self):

        geocodigo_uf =  self.kwargs.get("geocodigo")
        if geocodigo_uf is not None:
            return self.queryset.filter( geocodigo=geocodigo_uf )

        sigla_uf = self.kwargs.get("sigla")
        if sigla_uf is not None:
            return self.queryset.filter( sigla=sigla_uf.upper())

        siglas =  self.kwargs.get("siglas")
        if siglas is not None:
            return self.queryset.filter( sigla__in=siglas.split(",") )

        return super(UnidadeFederacaoFiltered, self).get_queryset()

class MunicipioList(CreatorContext):

    queryset = Municipio.objects.all()

    serializer_class = MunicipioSerializer

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'

class MunicipioFiltered(CreatorContext):

    queryset = Municipio.objects.all()

    serializer_class = MunicipioSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        nome_municipio = self.kwargs.get("nome")

        #sigla_uf = self.request.query_params.get('sigla', None)

        if nome_municipio is not None:

            return self.queryset.filter(nome=nome_municipio)


        return self.queryset

class OutrasUnidProtegidasList(CreatorContext):

    queryset = OutrasUnidProtegidas.objects.all()
    serializer_class = OutrasUnidProtegidasSerializer

class OutrosLimitesOficiaisList(CreatorContext):

    queryset = OutrosLimitesOficiais.objects.all()
    serializer_class = OutrosLimitesOficiaisSerializer

class PaisList(CreatorContext):

    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class TerraIndigenaList(CreatorContext):

    queryset = TerraIndigena.objects.all()
    serializer_class = TerraIndigenaSerializer

class UnidadeConservacaoNaoSnucList(CreatorContext):

    queryset = UnidadeConservacaoNaoSnuc.objects.all()
    serializer_class = UnidadeConservacaoNaoSnucSerializer

class UnidadeProtecaoIntegralList(CreatorContext):

    queryset = UnidadeProtecaoIntegral.objects.all()
    serializer_class = UnidadeProtecaoIntegralSerializer

class UnidadeUsoSustentavelList(CreatorContext):

    queryset = UnidadeUsoSustentavel.objects.all()
    serializer_class = UnidadeUsoSustentavelSerializer

class AglomeradoRuralDeExtensaoUrbanaList(CreatorContext):

    queryset = AglomeradoRuralDeExtensaoUrbana.objects.all()
    serializer_class = AglomeradoRuralDeExtensaoUrbanaSerializer

class AglomeradoRuralIsoladoList(CreatorContext):

    queryset = AglomeradoRuralIsolado.objects.all()
    serializer_class = AglomeradoRuralIsoladoSerializer

class AldeiaIndigenaList(CreatorContext):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer

class AldeiaIndigenaListFiltered(BasicListFiltered):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer

class AldeiaIndigenaListFilteredByQueryParameters(DefaultsMixin, ResourceListCreateFilteredByQueryParameters):
    serializer_class = AldeiaIndigenaSerializer

class AldeiaIndigenaDetail(APIViewDetailSpatialFunction):
    serializer_class = AldeiaIndigenaSerializer

class AreaEdificadaList(CreatorContext):

    queryset = AreaEdificada.objects.all()
    serializer_class = AreaEdificadaSerializer

class CapitalList(CreatorContext):

    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

class CidadeList(CreatorContext):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class VilaList(CreatorContext):

    queryset = Vila.objects.all()
    serializer_class = VilaSerializer

class CurvaBatimetricaList(CreatorContext):

    queryset = CurvaBatimetrica.objects.all()
    serializer_class = CurvaBatimetricaSerializer

class CurvaNivelList(CreatorContext):

    queryset = CurvaNivel.objects.all()
    serializer_class = CurvaNivelSerializer

class DunaList(CreatorContext):

    queryset = Duna.objects.all()
    serializer_class = DunaSerializer

class ElementoFisiograficoNaturalList(CreatorContext):

    queryset = ElementoFisiograficoNatural.objects.all()
    serializer_class = ElementoFisiograficoNaturalSerializer

class PicoList(CreatorContext):

    queryset = Pico.objects.all()
    serializer_class = PicoSerializer

class PontoCotadoAltimetricoList(CreatorContext):

    queryset = PontoCotadoAltimetrico.objects.all()
    serializer_class = PontoCotadoAltimetricoSerializer

class PontoCotadoBatimetricoList(CreatorContext):

    queryset = PontoCotadoBatimetrico.objects.all()
    serializer_class = PontoCotadoBatimetricoSerializer

class EclusaList(CreatorContext):

    queryset = Eclusa.objects.all()
    serializer_class = EclusaSerializer

class EdifConstPortuariaList(CreatorContext):

    queryset = EdifConstPortuaria.objects.all()
    serializer_class = EdifConstPortuariaSerializer

class EdifConstrAeroportuariaList(CreatorContext):

    queryset = EdifConstrAeroportuaria.objects.all()
    serializer_class = EdifConstrAeroportuariaSerializer

class EdifMetroFerroviariaList(CreatorContext):

    queryset = EdifMetroFerroviaria.objects.all()
    serializer_class = EdifMetroFerroviariaSerializer

class FundeadouroList(CreatorContext):

    queryset = Fundeadouro.objects.all()
    serializer_class = FundeadouroSerializer

class PistaPontoPousoList(CreatorContext):

    queryset = PistaPontoPouso.objects.all()
    serializer_class = PistaPontoPousoSerializer

class PonteList(CreatorContext):

    queryset = Ponte.objects.all()
    serializer_class = PonteSerializer

class SinalizacaoList(CreatorContext):

    queryset = Sinalizacao.objects.all()
    serializer_class = SinalizacaoSerializer

class TravessiaList(CreatorContext):

    queryset = Travessia.objects.all()
    serializer_class = TravessiaSerializer

class TrechoDutoList(CreatorContext):

    queryset = TrechoDuto.objects.all()
    serializer_class = TrechoDutoSerializer

class TrechoFerroviarioList(CreatorContext):

    queryset = TrechoFerroviario.objects.all()
    serializer_class = TrechoFerroviarioSerializer

class TrechoFerroviarioDetail(APIViewDetailSpatialFunction):
    """
    Retrieve, update or delete a unidades da federacao instance.
    """
    serializer_class = TrechoFerroviarioSerializer


class TrechoHidroviarioList(CreatorContext):

    queryset = TrechoHidroviario.objects.all()
    serializer_class = TrechoHidroviarioSerializer

class TrechoRodoviarioList(CreatorContext):

    queryset = TrechoRodoviario.objects.all()
    serializer_class = TrechoRodoviarioSerializer

class TunelList(CreatorContext):

    queryset = Tunel.objects.all()
    serializer_class = TunelSerializer

class BrejoPantanoList(CreatorContext):

    queryset = BrejoPantano.objects.all()
    serializer_class = BrejoPantanoSerializer

class MangueList(CreatorContext):

    queryset = Mangue.objects.all()
    serializer_class = MangueSerializer

class VegRestingaList(CreatorContext):

    queryset = VegRestinga.objects.all()
    serializer_class = VegRestingaSerializer

class EdifPubMilitarList(CreatorContext):

    queryset = EdifPubMilitar.objects.all()
    serializer_class = EdifPubMilitarSerializer

class PostoFiscalList(CreatorContext):

    queryset = PostoFiscal.objects.all()
    serializer_class = PostoFiscalSerializer

class EdifAgropecExtVegetalPescaList(CreatorContext):

    queryset = EdifAgropecExtVegetalPesca.objects.all()
    serializer_class = EdifAgropecExtVegetalPescaSerializer

class EdifIndustrialList(CreatorContext):

    queryset = EdifIndustrial.objects.all()
    serializer_class = EdifIndustrialSerializer

class ExtMineralList(CreatorContext):

    queryset = ExtMineral.objects.all()
    serializer_class = ExtMineralSerializer

class EdifReligiosaList(CreatorContext):

    queryset = EdifReligiosa.objects.all()
    serializer_class = EdifReligiosaSerializer

class EstGeradEnergiaEletricaList(CreatorContext):

    queryset = EstGeradEnergiaEletrica.objects.all()
    serializer_class = EstGeradEnergiaEletricaSerializer

class HidreletricaList(CreatorContext):

    queryset = Hidreletrica.objects.all()
    serializer_class = HidreletricaSerializer

class TermeletricaList(CreatorContext):

    queryset = Termeletrica.objects.all()
    serializer_class = TermeletricaSerializer

class TorreEnergiaList(CreatorContext):

    queryset = TorreEnergia.objects.all()
    serializer_class = TorreEnergiaSerializer

class BancoAreiaList(CreatorContext):

    queryset = BancoAreia.objects.all()
    serializer_class = BancoAreiaSerializer

class BarragemList(CreatorContext):

    queryset = Barragem.objects.all()
    serializer_class = BarragemSerializer

class CorredeiraList(CreatorContext):

    queryset = Corredeira.objects.all()
    serializer_class = CorredeiraSerializer

class FozMaritimaList(CreatorContext):

    queryset = FozMaritima.objects.all()
    serializer_class = FozMaritimaSerializer

class IlhaList(CreatorContext):

    queryset = Ilha.objects.all()
    serializer_class = IlhaSerializer

class MassaDaguaList(CreatorContext):

    queryset = MassaDagua.objects.all()
    serializer_class = MassaDaguaSerializer

class QuedaDaguaList(CreatorContext):

    queryset = QuedaDagua.objects.all()
    serializer_class = QuedaDaguaSerializer

class RecifeList(CreatorContext):

    queryset = Recife.objects.all()
    serializer_class = RecifeSerializer

class RochaEmAguaList(CreatorContext):

    queryset = RochaEmAgua.objects.all()
    serializer_class = RochaEmAguaSerializer

class SumidouroVertedouroList(CreatorContext):

    queryset = SumidouroVertedouro.objects.all()
    serializer_class = SumidouroVertedouroSerializer

class TerrenoSujeitoInundacaoList(CreatorContext):

    queryset = TerrenoSujeitoInundacao.objects.all()
    serializer_class = TerrenoSujeitoInundacaoSerializer

class TrechoDrenagemList(CreatorContext):

    queryset = TrechoDrenagem.objects.all()
    serializer_class = TrechoDrenagemSerializer

class TrechoMassaDaguaList(CreatorContext):

    queryset = TrechoMassaDagua.objects.all()
    serializer_class = TrechoMassaDaguaSerializer

class AreaDesenvolvimentoControleList(CreatorContext):

    queryset = AreaDesenvolvimentoControle.objects.all()
    serializer_class = AreaDesenvolvimentoControleSerializer

class MarcoDeLimiteList(CreatorContext):

    queryset = MarcoDeLimite.objects.all()
    serializer_class = MarcoDeLimiteSerializer

class PontoExibicaoWgs84List(CreatorContext):
    queryset = PontosExibicaoWgs84.objects.all()
    serializer_class = PontosExibicaoWgs84Serializer