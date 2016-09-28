from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.profile_list, name="profile_list"),
    url(r'^(?P<id>\d+)/$', views.user_profile, name="user_profile"),
    ]