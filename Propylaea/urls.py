from django.urls import re_path
from Propylaea import views

app_name = 'Propylaea'
urlpatterns = [
    re_path(r'^signup', views.SignUpV, name='signup'),
    re_path(r'^login', views.LogIn, name='login'),
    re_path(r'^logout', views.UsrLogout, name='logout')
]
