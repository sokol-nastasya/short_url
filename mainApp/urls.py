from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view()),
	url(r'^(?P<id_link>[\w-]+){6,15}/$', views.Links.as_view()),
	

]