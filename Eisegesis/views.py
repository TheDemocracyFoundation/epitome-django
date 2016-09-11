from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Proposals,ProposalChoice

@login_required
def index(request):
	latest_proposal_list = Proposals.objects.order_by('-P_CREATION')#[:5]
	template = loader.get_template('Eisegesis/index.html')
	context = {
		'latest_proposal_list': latest_proposal_list,
	}
	return HttpResponse(template.render(context, request))
	
	
@login_required
def moreInfo(request, proposals_id):
	proposal = get_object_or_404(Proposals, pk=proposals_id)
	#PChoice = get_object_or_404(ProposalChoice)
	template = loader.get_template('Eisegesis/propDetail.html')
	context = {
		'proposal': proposal,
		#'PChoice': PChoice,
	}
	#return render(request, 'polls/detail.html', {'question': question})
	return HttpResponse(template.render(context, request))

#def index(request):
#	return HttpResponse("Hello")

