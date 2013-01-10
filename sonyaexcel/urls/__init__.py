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
     url(r'^$', 'warehouse.views.home', name='home'),
    # url(r'^sonyaexcel/', include('sonyaexcel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


#Statics: Hacky for now... fix this later...
urlpatterns += patterns('',
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '/static/imgs/favicon.ico'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
