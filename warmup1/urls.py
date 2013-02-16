from django.conf.urls import patterns, include, url
from warmup1.models import userModel
from warmup1 import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'users/add', views.add),
    url(r'users/login', views.login),
    url(r'TESTAPI/resetFixture', views.TESTAPI_resetFixture),
    url(r'TESTAPI/unitTests', views.TESTAPI_unitTests),
    url(r'^(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': '/.'}),
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^proj1/', include('proj1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
