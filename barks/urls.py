from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.global_barks_list, name="global_barks_list"),
    url(r'^add/$', views.add_bark, name="add_bark"),
    url(r'^(?P<id>\d+)/$', views.barks_list, name="barks_list"),
]

#'^'' -> barks_list -> using user_id for specific user's barks
#'^' -> global -> every user's barks; needed?