from django.conf.urls import patterns, include, url

urlpatterns = patterns('flowers.views',
    url(r'^users/(?P<user_id>\d+)/*$', 'detail'),
    url(r'^users/*', 'list')
)
