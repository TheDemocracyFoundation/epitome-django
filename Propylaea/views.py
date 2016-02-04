from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


from Propylaea.forms import SignUp

def SignUpV(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUp(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUp()

    return render(request, 'signup.html', {'SignUpForm': form})
