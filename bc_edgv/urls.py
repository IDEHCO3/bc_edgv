from django.conf.urls import include, url
from hydra.urls import getHydraVocabURLPatterns

urlpatterns = [

    url(r'^instituicoes/ibge/bcim/', include('bcim.urls', namespace='bcim_v1')),
    url(r'^instituicoes/ibge/contexts/', include('context_api.urls', namespace='context')),
    getHydraVocabURLPatterns(r'^cartographicbase/hydra/'),


]
urlpatterns += [
    url(r'^instituicoes/ibge/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]