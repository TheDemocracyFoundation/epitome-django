from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from Demoscopesis.forms import PollForm, PollChoiceFormSet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import F

from .models import Poll, PollChoice, Voter


@login_required(login_url='/user/login/')
def index(request):
    poll_list = Poll.objects.order_by('-PL_CREATION')
    template = loader.get_template('Demoscopesis/index.html')
    paginator = Paginator(poll_list, 2)

    page = request.GET.get('page')
    latest_poll_list = paginator.get_page(page)

    context = {
        'latest_poll_list': latest_poll_list,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/user/login/')
def createPoll(request):
    template = loader.get_template('Demoscopesis/poll-edit.html')
    if request.method == 'GET':
        PollsForm = PollForm(request.GET or None)
        formset = PollChoiceFormSet(queryset=PollChoice.objects.none())
        context = {
            'PollForm': PollForm,
            'PollChoiceFormSet': formset,
        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        try:
            PollsForm = PollForm(request.POST)
            formset = PollChoiceFormSet(request.POST)
            if PollsForm.is_valid() and formset.is_valid():
                poll = PollsForm.save()
                for form in formset:
                    poll_choice = form.save(commit=False)
                    poll_choice.POLL = poll
                    poll_choice.save()
                return redirect('Demoscopesis:index')
        except:
            return HttpResponseRedirect(reverse('Demoscopesis:index'))


# if request.method == 'POST':
#	context = {
#		'PollForm': PollForm,
#		'PollChoiceFormSet' : formSet,
#	}
#	return HttpResponse(template.render(context, request))
# else:
#	formSet = PollChoiceFormSet
#	template = loader.get_template('Demoscopesis/poll-edit.html')
#	context = {
#		'PollForm': PollForm,
#		'PollChoiceFormSet' : formSet,
#	}
#	return HttpResponse(template.render(context, request))

@login_required(login_url='/user/login/')
def moreInfo(request, polls_id):
    poll = get_object_or_404(Poll, pk=polls_id)
    template = loader.get_template('Demoscopesis/poll.html')
    nowDt = timezone.localtime(timezone.now())
    context = {
        'poll': poll,
        'nowdt': nowDt,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/user/login/')
def vote(request, polls_id):
    poll = get_object_or_404(Poll, pk=polls_id)
    if Voter.objects.filter(POLL_id=polls_id, USER_id=request.user.id).exists():
        messages.add_message(request, messages.INFO, 'You have already voted.')
        return HttpResponseRedirect(reverse('Demoscopesis:index'))
    else:
        try:
            selected_choice = poll.PChoice.get(pk=request.POST['choice'])
        except (KeyError, PollChoice.DoesNotExist):  # probably wrong
            # Redisplay the question voting form.
            nowDt = timezone.localtime(timezone.now())
            return render(request, 'Demoscopesis/poll.html', {
                'poll': poll,
                'nowdt': nowDt,
                'error_message': "Please select a choice.",
            })
        else:
            selected_choice.PC_VOTES = F('PC_VOTES') + 1
            selected_choice.save()
            v = Voter(USER=request.user, POLL=poll)
            v.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            messages.add_message(request, messages.INFO, 'Vote submited successfully.')
            return HttpResponseRedirect(reverse('Demoscopesis:index'))  # , args=(poll.id,)))
