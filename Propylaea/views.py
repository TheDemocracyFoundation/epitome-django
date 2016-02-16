from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Propylaea.forms import UserForm, UserFormExtra

def SignUpV(request):
	# Signed up flag
	signedUp = False
	
    # If the request is type of POST then proccess data
	if request.method == 'POST':
        # Create 2 form instances and populate them with data from the POST request
		form1 = UserForm(request.POST)
		form2 = UserFormExtra(request.POST)
        # Check whether it's valid
		if form1.is_valid() and form2.is_valid():
			# Save main user form first and hash password
			try:
				user = form1.save(commit=False)
				user.set_password(user.password)
				user.save()
				# Save second form, where its id equals the user's
				profile = form2.save(commit=False)
				profile.user = user
				profile.save()
				# Change sign up flag to true
				signedUp = True
			except:
				signedUp = False
    # If request is not POST create empty forms
	else:
		form1 = UserForm()
		form2 = UserFormExtra()

	return render(request, 'signup.html', {'SignUpForm': form1, 'SignUpFormEx': form2})

def LogIn(request):
	# If the request is type of POST then proccess data
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		# Authenticate
		user = authenticate(email=email, password=password)
		# User valid
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse("Your account is loged in.")
			else:
				return HttpResponse("Your account is disabled.")
		else:
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'login.html', {})
