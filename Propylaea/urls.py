from django.conf.urls import url
from Propylaea import views

urlpatterns = [
    #~ url(r'^$', views.UserIndex, name='index'),
    url(r'^signup', views.SignUpV, name='signup')
    #~ url(r'^/login', views.LogIn, name='login')
]
