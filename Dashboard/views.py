from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


@login_required(login_url='/user/login/')
def index(request):
    template = loader.get_template('Dashboard/home.html')
    return HttpResponse(template.render({},request))