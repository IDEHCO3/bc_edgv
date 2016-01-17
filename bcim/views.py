import httplib2
import json as json
from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework_gis import filters
from rest_framework_gis.filterset import GeoFilterSet
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




@api_view(('GET',))
def api_root(request, format=None):
    return Response({
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

class DefaultsMixin(object):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    paginate_by = 250

    # Default settings for view authentication, permissions, filtering and pagination.
"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
"""

class ResourceListCreateFilteredByQueryParameters(generics.ListCreateAPIView):

    def get_queryset(self):
        model_class = self.serializer_class.Meta.model
        queryset = model_class.objects.all()
        query_parameters = self.request.query_params
        dict = self.get_dict_with_spatialfunction_or_same_dict(query_parameters.dict())

        queryset = queryset.filter(**dict)
        return queryset

    def get_dict_with_spatialfunction_or_same_dict(self, dict):
        for key, value in dict.items():
            if key.startswith('*'):
                new_key = self.serializer_class.Meta.geo_field + '__' + key[1:]
                dict.pop(key)
                #a_value = value
                #a_geom = GEOSGeometry(a_value, 4326)
                dict[new_key] = value
        return dict



class BasicListFiltered(generics.ListCreateAPIView):

    def get_queryset(self):

        st_function = self.kwargs.get("spatial_function")
        geom_str_or_url = self.kwargs.get('geom')
        url_rest = self.request.query_params.get('url', None)
        a_key = self.serializer_class.Meta.geo_field + '__' + st_function
        aGeom = self.geos_geometry(geom_str_or_url)

        if st_function is not None:
            model_class = self.serializer_class.Meta.model
            return model_class.objects.filter(**({a_key: aGeom}))

        return self.queryset

    def geos_geometry(self, geom_str_or_url):
        a_geom =  geom_str_or_url
        str1 = (geom_str_or_url[0:5]).upper()
        str2 = 'http:'.upper()
        if (str1 == str2):
            h = httplib2.Http(".cache")
            resp, a_geom = h.request(geom_str_or_url, "GET")
            a_geojson = json.loads(a_geom.decode())
            a_geom = (a_geojson["features"][0]["geometry"]).__str__()
        return GEOSGeometry(a_geom, 4326)
class APIViewDetailSpatialFunction(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def model_class(self):
        return self.serializer_class.Meta.model

    def geometry_field_name(self):
        return self.serializer_class.Meta.geo_field

    def spatial_function_name_template(self):
        return 'spatial_function'

    def spatial_function_parameter_template(self):
        return 'param'

    def get_object(self, a_dict):
        queryset = self.model_class().objects.all()
        obj = get_object_or_404(queryset, **a_dict)
        self.check_object_permissions(self.request, obj)
        return obj

    def dic_with_only_identitier_field(self):
        a_dict = {}
        for key, value in self.kwargs.items():
            if key != self.spatial_function_name_template() and key != self.spatial_function_parameter_template():
                a_dict[key] = value
                break
        return a_dict

    def get_geometry_object(self, object_model):
        return getattr(object_model, self.geometry_field_name(), None)


    def parametersConverted(self, params_as_comma_string):
        paramsConveted = []
        params_as_array = params_as_comma_string.split(',')
        for value in params_as_array:
            if value.lower() == 'true':
                paramsConveted.append(True)
                continue
            elif value.lower() == 'false':
                paramsConveted.append(False)
                continue

            try:
                paramsConveted.append(int( value ) )
            except ValueError:
                try:
                    paramsConveted.append( float( value ) )
                except ValueError:
                    paramsConveted.append ( value)
        return paramsConveted

    def get(self, request, *args, **kwargs):

        object_model = self.get_object(self.dic_with_only_identitier_field())
        st_function = self.kwargs.get(self.spatial_function_name_template())
        if not st_function:
           serializer = self.serializer_class(object_model)
           return Response(serializer.data)

        param = self.kwargs.get(self.spatial_function_parameter_template())
        if param:
            params = self.parametersConverted(param)
            res = getattr(self.get_geometry_object(object_model), st_function)(*params)
        else:
            res = getattr(self.get_geometry_object(object_model), st_function)

        if isinstance(res, GEOSGeometry):
            return HttpResponse(res.geojson)

        a_dict = {st_function : res}
        return Response(a_dict)

class UnidadeFederacaoDetail(APIViewDetailSpatialFunction):
    """
    Retrieve, update or delete a unidades da federação instance.
    """
    serializer_class = UnidadeFederacaoSerializer


class UnidadeFederacaoDetailOLD1(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self):
        queryset = UnidadeFederacao.objects.all()
        filter = {}
        #for field in self.multiple_lookup_fields:
        #    filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **self.kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        uf = self.get_object()
        serializer = UnidadeFederacaoSerializer(uf)
        return Response(serializer.data)


class UnidadeFederacaoDetailSpatial(APIViewDetailSpatialFunction):
    serializer_class = UnidadeFederacaoSerializer

class UnidadeFederacaoDetailSpatialOld(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, a_dict):
        queryset = UnidadeFederacao.objects.all()
        obj = get_object_or_404(queryset, **a_dict)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        st_function = self.kwargs.get('spatial_function')
        param = self.kwargs.get('param')
        a_dict = {}
        for key, value in self.kwargs.items():
            if key != 'spatial_function' and key != 'param':
                a_dict[key] = value
                break
        uf = self.get_object(a_dict)
        if param:
            res = getattr(uf.geom,st_function)(param)
        else:
            res = getattr(uf.geom,st_function)
            if callable(res):
                res = res(param)
        a_dict = {st_function : res}

        return Response(json.dumps(a_dict))

class UnidadeFederacaoList(generics.ListCreateAPIView):
    queryset = UnidadeFederacao.objects.all()
    serializer_class = UnidadeFederacaoSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UnidadeFederacaoListFilteredByQueryParameters(DefaultsMixin, ResourceListCreateFilteredByQueryParameters):
    """API endpoint for listing and creating sprints."""
    serializer_class = UnidadeFederacaoSerializer


class UnidadeFederacaoFiltered(BasicListFiltered):

    queryset = UnidadeFederacao.objects.all()

    serializer_class = UnidadeFederacaoSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
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



class MunicipioList(generics.ListCreateAPIView):

    queryset = Municipio.objects.all()

    serializer_class = MunicipioSerializer

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'

class MunicipioFiltered(generics.ListCreateAPIView):

    queryset = Municipio.objects.all()

    serializer_class = MunicipioSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        nome_municipio = self.kwargs.get("nome")

        #sigla_uf = self.request.query_params.get('sigla', None)

        if nome_municipio is not None:

            return self.queryset.filter(nome=nome_municipio)


        return self.queryset

class OutrasUnidProtegidasList(generics.ListCreateAPIView):

    queryset = OutrasUnidProtegidas.objects.all()
    serializer_class = OutrasUnidProtegidasSerializer

class OutrosLimitesOficiaisList(generics.ListCreateAPIView):

    queryset = OutrosLimitesOficiais.objects.all()
    serializer_class = OutrosLimitesOficiaisSerializer

class PaisList(generics.ListCreateAPIView):

    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class TerraIndigenaList(generics.ListCreateAPIView):

    queryset = TerraIndigena.objects.all()
    serializer_class = TerraIndigenaSerializer

class UnidadeConservacaoNaoSnucList(generics.ListCreateAPIView):

    queryset = UnidadeConservacaoNaoSnuc.objects.all()
    serializer_class = UnidadeConservacaoNaoSnucSerializer

class UnidadeProtecaoIntegralList(generics.ListCreateAPIView):

    queryset = UnidadeProtecaoIntegral.objects.all()
    serializer_class = UnidadeProtecaoIntegralSerializer

class UnidadeUsoSustentavelList(generics.ListCreateAPIView):

    queryset = UnidadeUsoSustentavel.objects.all()
    serializer_class = UnidadeUsoSustentavelSerializer

class AglomeradoRuralDeExtensaoUrbanaList(generics.ListCreateAPIView):

    queryset = AglomeradoRuralDeExtensaoUrbana.objects.all()
    serializer_class = AglomeradoRuralDeExtensaoUrbanaSerializer

class AglomeradoRuralIsoladoList(generics.ListCreateAPIView):

    queryset = AglomeradoRuralIsolado.objects.all()
    serializer_class = AglomeradoRuralIsoladoSerializer

class AldeiaIndigenaList(generics.ListCreateAPIView):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer

class AldeiaIndigenaListFiltered(BasicListFiltered):

    queryset = AldeiaIndigena.objects.all()
    serializer_class = AldeiaIndigenaSerializer


class AldeiaIndigenaDetail(APIViewDetailSpatialFunction):

    serializer_class = AldeiaIndigenaSerializer


class AreaEdificadaList(generics.ListCreateAPIView):

    queryset = AreaEdificada.objects.all()
    serializer_class = AreaEdificadaSerializer

class CapitalList(generics.ListCreateAPIView):

    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

class CidadeList(generics.ListCreateAPIView):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class VilaList(generics.ListCreateAPIView):

    queryset = Vila.objects.all()
    serializer_class = VilaSerializer

class CurvaBatimetricaList(generics.ListCreateAPIView):

    queryset = CurvaBatimetrica.objects.all()
    serializer_class = CurvaBatimetricaSerializer

class CurvaNivelList(generics.ListCreateAPIView):

    queryset = CurvaNivel.objects.all()
    serializer_class = CurvaNivelSerializer

class DunaList(generics.ListCreateAPIView):

    queryset = Duna.objects.all()
    serializer_class = DunaSerializer

class ElementoFisiograficoNaturalList(generics.ListCreateAPIView):

    queryset = ElementoFisiograficoNatural.objects.all()
    serializer_class = ElementoFisiograficoNaturalSerializer

class PicoList(generics.ListCreateAPIView):

    queryset = Pico.objects.all()
    serializer_class = PicoSerializer

class PontoCotadoAltimetricoList(generics.ListCreateAPIView):

    queryset = PontoCotadoAltimetrico.objects.all()
    serializer_class = PontoCotadoAltimetricoSerializer

class PontoCotadoBatimetricoList(generics.ListCreateAPIView):

    queryset = PontoCotadoBatimetrico.objects.all()
    serializer_class = PontoCotadoBatimetricoSerializer

class EclusaList(generics.ListCreateAPIView):

    queryset = Eclusa.objects.all()
    serializer_class = EclusaSerializer

class EdifConstPortuariaList(generics.ListCreateAPIView):

    queryset = EdifConstPortuaria.objects.all()
    serializer_class = EdifConstPortuariaSerializer

class EdifConstrAeroportuariaList(generics.ListCreateAPIView):

    queryset = EdifConstrAeroportuaria.objects.all()
    serializer_class = EdifConstrAeroportuariaSerializer

class EdifMetroFerroviariaList(generics.ListCreateAPIView):

    queryset = EdifMetroFerroviaria.objects.all()
    serializer_class = EdifMetroFerroviariaSerializer

class FundeadouroList(generics.ListCreateAPIView):

    queryset = Fundeadouro.objects.all()
    serializer_class = FundeadouroSerializer

class PistaPontoPousoList(generics.ListCreateAPIView):

    queryset = PistaPontoPouso.objects.all()
    serializer_class = PistaPontoPousoSerializer

class PonteList(generics.ListCreateAPIView):

    queryset = Ponte.objects.all()
    serializer_class = PonteSerializer

class SinalizacaoList(generics.ListCreateAPIView):

    queryset = Sinalizacao.objects.all()
    serializer_class = SinalizacaoSerializer

class TravessiaList(generics.ListCreateAPIView):

    queryset = Travessia.objects.all()
    serializer_class = TravessiaSerializer

class TrechoDutoList(generics.ListCreateAPIView):

    queryset = TrechoDuto.objects.all()
    serializer_class = TrechoDutoSerializer

class TrechoFerroviarioList(generics.ListCreateAPIView):

    queryset = TrechoFerroviario.objects.all()
    serializer_class = TrechoFerroviarioSerializer

class TrechoHidroviarioList(generics.ListCreateAPIView):

    queryset = TrechoHidroviario.objects.all()
    serializer_class = TrechoHidroviarioSerializer

class TrechoRodoviarioList(generics.ListCreateAPIView):

    queryset = TrechoRodoviario.objects.all()
    serializer_class = TrechoRodoviarioSerializer

class TunelList(generics.ListCreateAPIView):

    queryset = Tunel.objects.all()
    serializer_class = TunelSerializer

class BrejoPantanoList(generics.ListCreateAPIView):

    queryset = BrejoPantano.objects.all()
    serializer_class = BrejoPantanoSerializer

class MangueList(generics.ListCreateAPIView):

    queryset = Mangue.objects.all()
    serializer_class = MangueSerializer

class VegRestingaList(generics.ListCreateAPIView):

    queryset = VegRestinga.objects.all()
    serializer_class = VegRestingaSerializer

class EdifPubMilitarList(generics.ListCreateAPIView):

    queryset = EdifPubMilitar.objects.all()
    serializer_class = EdifPubMilitarSerializer

class PostoFiscalList(generics.ListCreateAPIView):

    queryset = PostoFiscal.objects.all()
    serializer_class = PostoFiscalSerializer

class EdifAgropecExtVegetalPescaList(generics.ListCreateAPIView):

    queryset = EdifAgropecExtVegetalPesca.objects.all()
    serializer_class = EdifAgropecExtVegetalPescaSerializer

class EdifIndustrialList(generics.ListCreateAPIView):

    queryset = EdifIndustrial.objects.all()
    serializer_class = EdifIndustrialSerializer

class ExtMineralList(generics.ListCreateAPIView):

    queryset = ExtMineral.objects.all()
    serializer_class = ExtMineralSerializer

class EdifReligiosaList(generics.ListCreateAPIView):

    queryset = EdifReligiosa.objects.all()
    serializer_class = EdifReligiosaSerializer

class EstGeradEnergiaEletricaList(generics.ListCreateAPIView):

    queryset = EstGeradEnergiaEletrica.objects.all()
    serializer_class = EstGeradEnergiaEletricaSerializer

class HidreletricaList(generics.ListCreateAPIView):

    queryset = Hidreletrica.objects.all()
    serializer_class = HidreletricaSerializer

class TermeletricaList(generics.ListCreateAPIView):

    queryset = Termeletrica.objects.all()
    serializer_class = TermeletricaSerializer

class TorreEnergiaList(generics.ListCreateAPIView):

    queryset = TorreEnergia.objects.all()
    serializer_class = TorreEnergiaSerializer

class BancoAreiaList(generics.ListCreateAPIView):

    queryset = BancoAreia.objects.all()
    serializer_class = BancoAreiaSerializer

class BarragemList(generics.ListCreateAPIView):

    queryset = Barragem.objects.all()
    serializer_class = BarragemSerializer

class CorredeiraList(generics.ListCreateAPIView):

    queryset = Corredeira.objects.all()
    serializer_class = CorredeiraSerializer

class FozMaritimaList(generics.ListCreateAPIView):

    queryset = FozMaritima.objects.all()
    serializer_class = FozMaritimaSerializer

class IlhaList(generics.ListCreateAPIView):

    queryset = Ilha.objects.all()
    serializer_class = IlhaSerializer

class MassaDaguaList(generics.ListCreateAPIView):

    queryset = MassaDagua.objects.all()
    serializer_class = MassaDaguaSerializer

class QuedaDaguaList(generics.ListCreateAPIView):

    queryset = QuedaDagua.objects.all()
    serializer_class = QuedaDaguaSerializer

class RecifeList(generics.ListCreateAPIView):

    queryset = Recife.objects.all()
    serializer_class = RecifeSerializer

class RochaEmAguaList(generics.ListCreateAPIView):

    queryset = RochaEmAgua.objects.all()
    serializer_class = RochaEmAguaSerializer

class SumidouroVertedouroList(generics.ListCreateAPIView):

    queryset = SumidouroVertedouro.objects.all()
    serializer_class = SumidouroVertedouroSerializer

class TerrenoSujeitoInundacaoList(generics.ListCreateAPIView):

    queryset = TerrenoSujeitoInundacao.objects.all()
    serializer_class = TerrenoSujeitoInundacaoSerializer

class TrechoDrenagemList(generics.ListCreateAPIView):

    queryset = TrechoDrenagem.objects.all()
    serializer_class = TrechoDrenagemSerializer

class TrechoMassaDaguaList(generics.ListCreateAPIView):

    queryset = TrechoMassaDagua.objects.all()
    serializer_class = TrechoMassaDaguaSerializer

class AreaDesenvolvimentoControleList(generics.ListCreateAPIView):

    queryset = AreaDesenvolvimentoControle.objects.all()
    serializer_class = AreaDesenvolvimentoControleSerializer

class MarcoDeLimiteList(generics.ListCreateAPIView):

    queryset = MarcoDeLimite.objects.all()
    serializer_class = MarcoDeLimiteSerializer

class PontoExibicaoWgs84List(generics.ListCreateAPIView):
    queryset = PontosExibicaoWgs84.objects.all();
    serializer_class = PontosExibicaoWgs84Serializer