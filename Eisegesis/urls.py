from django.conf.urls import url
from Eisegesis import views
from django.urls import path
from django.contrib import admin

app_name = 'Eisegesis'
urlpatterns = [
	#/eisegesis/
	url(r'^$', views.index, name='index'),
	#/eisegesis/5/
	url(r'^(?P<polls_id>[0-9]+)/$', views.moreInfo, name='moreInfo'),
	#/eisegesis/5/vote
	url(r'^(?P<polls_id>[0-9]+)/vote/$', views.vote, name='vote'),
	#/eisegesis/create
	url(r'^create/$', views.createPoll, name='createPoll'),
	#/eisegesis/edit/5/
	#url(r'^/edit/(?P<polls_id>[0-9]+)/$', views.edit, name='edit'),
]

admin.site.site_header = 'Epitome administration'
admin.site.site_title = 'Epitome administration'
admin.site.index_title = 'Home'
