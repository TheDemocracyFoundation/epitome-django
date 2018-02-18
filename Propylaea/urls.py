from django.conf.urls import url
from Propylaea import views

app_name = 'Propylaea'
urlpatterns = [
    #~ url(r'^$', views.UserIndex, name='index'),
    url(r'^signup', views.SignUpV, name='signup'),
    url(r'^login', views.LogIn, name='login'),
    url(r'^logout', views.UsrLogout, name='logout')
]
