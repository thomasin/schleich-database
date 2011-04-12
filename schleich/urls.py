import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^schleich/', include('schleich.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^catalogue/(?P<name>.*)$', 'schleich.catalogue.views.name'),
    (r'^index.html$', 'schleich.catalogue.views.home'),
    (r'^stats.html$', 'schleich.catalogue.views.statistics'),
    (r'^gallery.html$', 'schleich.catalogue.views.gallery'),
    (r'^lists.html$', 'schleich.catalogue.views.lists'),
    
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, 'images')}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, 'css')}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, 'js')}),
    (r'^admin/', include(admin.site.urls)),
)
