"""Epitome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Agora import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.homePage, name='home'),
    url(r'^user/', include('Propylaea.urls', namespace="Propylaea")),
    url(r'^eisegesis/', include('Eisegesis.urls', namespace="Eisegesis")),
    url(r'^.*/$', RedirectView.as_view(url='/home/')),
    url(r'^$', RedirectView.as_view(url='/home/'))
]

urlpatterns += staticfiles_urlpatterns()
