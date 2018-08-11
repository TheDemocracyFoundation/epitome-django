from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.views import generic

#~ from .forms import RegForm


def aboutPage(request):
   return render(request, 'about.html')
