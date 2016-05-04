from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'^idehco3/bcedgv/ibge/bcim/', include('bcim.urls', namespace='bcim_v1')),
    url(r'^idehco3/bcedgv/contexts/', include('context.urls', namespace='context')),


]
urlpatterns += [
    url(r'^idehco3/bcedgv/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]