from django.conf.urls import include, url
import sys

from hydra.urls import getHydraVocabURLPatterns
basic_path = 'instituicoes/ibge/bcim/'
basic_path_context = 'instituicoes/ibge/contexts/'
basic_path_hydra = 'instituicoes/ibge/hydra/'

host_name = sys.argv[-1]
protocol = 'http'

urlpatterns = [

    url(r'^'+ basic_path, include('bcim.urls', namespace='bcim_v1')),
    url(r'^'+ basic_path_context, include('context_api.urls', namespace='context')),
    getHydraVocabURLPatterns(r'^'+ basic_path_hydra),


]