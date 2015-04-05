from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
from peminjaman import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^peminjaman/', include('peminjaman.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
