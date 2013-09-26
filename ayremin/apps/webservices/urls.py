from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ayremin.apps.webservices.views',
	url(r'^ws/matriculas$', 'wsMatriculas_view',name = 'ws_productos_urls'),
)