from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^(?P<user_id>\d+)/*$', 'detail', {}, 'detail'),
    url(r'^.*', 'list', {}, 'list')
)