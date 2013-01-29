from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('flowers.views',
    url(r'^users/(?P<user_id>\d+)/*$', 'detail'),
    url(r'^users/*', 'list')
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls))
)
