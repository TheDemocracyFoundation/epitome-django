from django.conf.urls import url
from Demoscopesis import views
#from django.urls import path
from django.contrib import admin

app_name = 'Demoscopesis'
urlpatterns = [
	#/Demoscopesis/
	url(r'^$', views.index, name='index'),
	#/Demoscopesis/5/
	url(r'^(?P<polls_id>[0-9]+)/$', views.moreInfo, name='moreInfo'),
	#/Demoscopesis/5/vote
	url(r'^(?P<polls_id>[0-9]+)/vote/$', views.vote, name='vote'),
	#/Demoscopesis/create
	url(r'^create/$', views.createPoll, name='createPoll'),
	#/Demoscopesis/edit/5/
	#url(r'^/edit/(?P<polls_id>[0-9]+)/$', views.edit, name='edit'),
]

admin.site.site_header = 'Epitome administration'
admin.site.site_title = 'Epitome administration'
admin.site.index_title = 'Home'
