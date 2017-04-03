from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import Proposals,ProposalChoice,Voter

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
	template = loader.get_template('Eisegesis/proposal.html')
	nowDt = timezone.localtime(timezone.now())
	context = {
		'proposal': proposal,
		'nowdt': nowDt,
		#'PChoice': PChoice,
	}
	#return render(request, 'polls/detail.html', {'question': question})
	return HttpResponse(template.render(context, request))

@login_required
def vote(request, proposals_id):
	proposal = get_object_or_404(Proposals, pk=proposals_id)
	if Voter.objects.filter(Proposals_id=proposals_id, user_id=request.user.id).exists():
		messages.add_message(request, messages.INFO, 'You have already voted.')
		return HttpResponseRedirect(reverse('Eisegesis:index'))#, args=(proposal.id,)))
	else:
		try:
			selected_choice = proposal.PChoice.get(pk=request.POST['choice'])
		except (KeyError, ProposalChoice.DoesNotExist):						#probably wrong
			# Redisplay the question voting form.
			nowDt = timezone.localtime(timezone.now())
			return render(request, 'Eisegesis/proposal.html', {
				#'question': question,
				'proposal': proposal,
				'nowdt': nowDt,
				'error_message': "You didn't select a choice.",
			})
		else:
			selected_choice.PCHOICE_VOTES += 1
			selected_choice.save()
			v = Voter(user=request.user, Proposals=proposal)
			v.save()
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			messages.add_message(request, messages.INFO, 'Vote submited successfully.')
			return HttpResponseRedirect(reverse('Eisegesis:index'))#, args=(proposal.id,)))

#def index(request):
#	return HttpResponse("Hello")

