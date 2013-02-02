from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^login', 'homepage.views.login', name='login'),
    url(r'^logout', 'homepage.views.logout', name='logout'),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls))
)
