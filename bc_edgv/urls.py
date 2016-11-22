from django.conf.urls import include, url
from hydra.urls import getHydraVocabURLPatterns

urlpatterns = [

    url(r'^idehco3/bcedgv/ibge/bcim/', include('bcim.urls', namespace='bcim_v1')),
    url(r'^idehco3/bcedgv/contexts/', include('context_api.urls', namespace='context')),
    getHydraVocabURLPatterns(r'^idehco3/bcedgv/hydra/'),


]
urlpatterns += [
    url(r'^idehco3/bcedgv/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]