from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users?/$', views.global_barks_list, name="global_barks_list"),
    url(r'^add/$', views.add_bark, name="add_bark"),
    url(r'^(?P<id>\d+)/$', views.barks_list, name="barks_list"),
    url(r'^$', views.barks_list, name="barks_list"),
]