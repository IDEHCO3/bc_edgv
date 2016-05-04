
from django.conf.urls import patterns, url
from context import views


urlpatterns = patterns('',
    url(r'^(?P<classname>.+)\.jsonld$', views.ContextView.as_view(), name='detail'),
)