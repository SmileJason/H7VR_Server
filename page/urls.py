from django.conf.urls import patterns, url


urlpatterns = patterns('page.views',
    url(r'^photo_upload/$', 'upload_image'),
    
    url(r'^(?P<page_id>\d+)/preview/$', 'preview_page', name='page-preview'),

    url(r'^(?P<slug>[^/]+)/$', 'get_page', name='page-detail'),

)
