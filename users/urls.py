from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^(?P<user_id>\d+)/*$', 'detail', name='detail'),
    url(r'^create', 'create', name='create'),
    url(r'^.*', 'list', name='list')
)