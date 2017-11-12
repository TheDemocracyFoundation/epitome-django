from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import Polls,PollChoice,Voter

@login_required
def index(request):
	latest_poll_list = Polls.objects.order_by('-P_CREATION')#[:5]
	template = loader.get_template('Eisegesis/index.html')
	context = {
		'latest_poll_list': latest_poll_list,
	}
	return HttpResponse(template.render(context, request))


@login_required
def moreInfo(request, polls_id):
	poll = get_object_or_404(Polls, pk=polls_id)
	#PChoice = get_object_or_404(PollChoice)
	template = loader.get_template('Eisegesis/poll.html')
	nowDt = timezone.localtime(timezone.now())
	context = {
		'poll': poll,
		'nowdt': nowDt,
		#'PChoice': PChoice,
	}
	#return render(request, 'polls/detail.html', {'question': question})
	return HttpResponse(template.render(context, request))

@login_required
def vote(request, polls_id):
	poll = get_object_or_404(Polls, pk=polls_id)
	if Voter.objects.filter(Polls_id=polls_id, user_id=request.user.id).exists():
		messages.add_message(request, messages.INFO, 'You have already voted.')
		return HttpResponseRedirect(reverse('Eisegesis:index'))#, args=(poll.id,)))
	else:
		try:
			selected_choice = poll.PChoice.get(pk=request.POST['choice'])
		except (KeyError, PollChoice.DoesNotExist):						#probably wrong
			# Redisplay the question voting form.
			nowDt = timezone.localtime(timezone.now())
			return render(request, 'Eisegesis/poll.html', {
				#'question': question,
				'poll': poll,
				'nowdt': nowDt,
				'error_message': "You didn't select a choice.",
			})
		else:
			selected_choice.PCHOICE_VOTES += 1
			selected_choice.save()
			v = Voter(user=request.user, Polls=poll)
			v.save()
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			messages.add_message(request, messages.INFO, 'Vote submited successfully.')
			return HttpResponseRedirect(reverse('Eisegesis:index'))#, args=(poll.id,)))

#def index(request):
#	return HttpResponse("Hello")

