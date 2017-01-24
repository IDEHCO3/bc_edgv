from django.conf.urls import include, url
from hydra.urls import getHydraVocabURLPatterns

urlpatterns = [

    url(r'^cartographicbase/ibge/bcim/', include('bcim.urls', namespace='bcim_v1')),
    url(r'^cartographicbase/contexts/', include('context_api.urls', namespace='context')),
    getHydraVocabURLPatterns(r'^cartographicbase/hydra/'),


]
urlpatterns += [
    url(r'^cartographicbase/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]