from django.conf.urls import patterns, url

from agg import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
