from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from Demoscopesis.models import Poll


@login_required(login_url='/user/login/')
def index(request):
    template = loader.get_template('Episkopesis/home.html')
    request.activeCount = Poll.objects.filter(PL_ENDDT__gt=datetime.now()).count()
    request.inactiveCount = Poll.objects.filter(PL_ENDDT__lt=datetime.now()).count()
    return HttpResponse(template.render({}, request))
