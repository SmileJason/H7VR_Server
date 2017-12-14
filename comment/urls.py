from django.conf.urls import patterns, url


urlpatterns = patterns('comment.views',
    url(r'^page/(?P<page_id>\d+)/$', 'comment_page', name='page-comment'),
)
