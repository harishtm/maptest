from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^apptest/', include('apptest.urls')),
    url(r'^mymap/', 'tmap.views.myhome',name="mymap"),
    url(r'^address/', 'tmap.views.capture_address',name="capture_address"),
    url(r'scroll/','tmap.views.scroll',name="scroll")
)
