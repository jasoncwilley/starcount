from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^hotelsite/', include('hotelsite.urls', namespace="hotelsite")),
    url(r'^admin/', include(admin.site.urls)),
	url('^accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),
]

