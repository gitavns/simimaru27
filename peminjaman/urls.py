from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'peminjaman.views2.index', name='peminjaman'),
    url(r'^history', 'peminjaman.views.history', name='history'),
    url(r'^history/export', 'peminjaman.views.export', name='export'),
    url(r'^create', 'peminjaman.views.create', name='create'),
    url(r'^ruangan', 'peminjaman.views3.ruangan', name='ruangan'),
    #url(r'^sukses', 'peminjaman.views2.sukses', name='sukses'),
    url(r'^suksesdetail', 'peminjaman.views4.suksesdetail', name='suksesdetail'),
    url(r'^detail', 'peminjaman.views4.detail', name='detail'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login', 'peminjaman.views4.login', name='login'),
    
    url(r'^import', 'peminjaman.views4.importjadwal', name='importjadwal'),
    url(r'^baru', 'peminjaman.views4.baru', name='baru'),
    url(r'^alur', 'peminjaman.views4.alur', name='alur'),
    url(r'^update', 'peminjaman.views2.update', name='update'),
    url(r'^ubah', 'peminjaman.views2.ubah', name='ubah'),
    url(r'^sukses', 'peminjaman.views2.sukses', name='sukses'),
    url(r'^delete', 'peminjaman.views2.delete', name='delete'),
)
