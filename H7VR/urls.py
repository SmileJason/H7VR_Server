"""H7VR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import H7VR.views as view

urlpatterns = [
    
    url(r'^$', 'common.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^articles/', include('page.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    url(r'^.well-known/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    url(r'^api/', include('api.urls')),

    url(r'^vr3d/', include('vr3d.urls')),

]

handler404 = view.page_not_found

handler500 = view.page_error
