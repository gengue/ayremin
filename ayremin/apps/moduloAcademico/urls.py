from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ayremin.apps.moduloAcademico.views',
	url(r'^$','login_view', name='vista_login'),
	url(r'^logout/$', 'logout_view',name = 'vista_logout'),
	url(r'^hojadevida/$', 'hojadevida_view',name = 'vista_hojadevida'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^miInfo/$','info_view', name='vista_info'),
)