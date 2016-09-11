from django.conf.urls import url
from Eisegesis import views

urlpatterns = [
	#/eisegesis/
	url(r'^$', views.index, name='index'),
	#/eisegesis/5/
	url(r'^(?P<proposals_id>[0-9]+)/$', views.moreInfo, name='moreInfo'),
	#/eisegesis/5/vote
	#url(r'^(?P<proposals_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
