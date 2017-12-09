from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.views import generic

#~ from .forms import RegForm


def homePage(request):
   return render(request, 'home.html')
