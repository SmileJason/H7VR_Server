from django.conf.urls import patterns, url


urlpatterns = patterns('vr3d.views',
    url(r'^vr/show/$', 'vr_show', name='vr-show'),
)
