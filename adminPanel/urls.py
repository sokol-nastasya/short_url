from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^adminPanel/$', views.adminPanel, name = 'adminPanel'),
	url(r'^details/(?P<pk>\d+)/$', views.details, name = 'details'), 
	url(r'^edit/(?P<url_id>\d+)/$', views.editUrl, name = 'editUrl'),
	url(r'^edit/(?P<pk>[0-9]+)/delete/$', views.delete, name='delete_object'),
	

]