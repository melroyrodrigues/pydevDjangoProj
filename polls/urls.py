import views

from django.conf.urls import url


urlpatterns = [
				 url(r'^$', views.index, name='index'),
				 url(r'^(?P<q_id>[0-9]+)/detail/$', views.detail, name='detail'),
				 url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
				 url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results')
				 ]
