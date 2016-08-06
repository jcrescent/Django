from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.create),
    url(r'^goback$', views.back),
    url(r'^remove/(?P<id>[0-9])/$', views.show),
    url(r'^delete/(?P<id>\d+)/$', views.delete)
]