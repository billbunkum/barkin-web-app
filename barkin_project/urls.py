from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^barks/', include('barks.urls', namespace='barks')),
    url(r'^', include('core.urls', namespace='core')),
]
