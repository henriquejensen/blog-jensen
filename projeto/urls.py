from django.conf.urls import patterns, url
from projeto import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.getpost, name='getpost'),
)
