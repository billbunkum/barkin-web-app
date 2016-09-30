from django.conf.urls import include, url

from .forms import LoginForm
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'authentication_form': LoginForm}, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^profile/$', include('barks.urls'), name='profile')
]