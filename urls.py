from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('doziefoodtruck.urls')),
    (r'^api/', include('api.urls')),
    (r'^admin/(.*)', admin.site.root),
)
