from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'peminjaman.views.index', name='peminjaman'),
    url(r'^history', 'peminjaman.views.history', name='history'),
    url(r'^create', 'peminjaman.views.create', name='create'),
    url(r'^ruangan', 'peminjaman.views.ruangan', name='ruangan'),
    #url(r'^sukses', 'peminjaman.views2.sukses', name='sukses'),
    url(r'^suksesdetail', 'peminjaman.views4.suksesdetail', name='suksesdetail'),
    url(r'^detail', 'peminjaman.views4.detail', name='detail'),
    # url(r'^blog/', include('blog.urls')),

)
