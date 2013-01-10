from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'sonyaexcel.views.page_not_found_error'
handler500 = 'sonyaexcel.views.server_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sonyaexcel.views.home', name='home'),
    # url(r'^sonyaexcel/', include('sonyaexcel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
