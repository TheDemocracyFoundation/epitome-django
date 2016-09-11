from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Propylaea.forms import LoginForm, SignUpForm
from django.template import loader
from django.contrib.auth.decorators import login_required

def SignUpV(request):
	# Signed up flag
	signedUp = False
	
    # If the request is type of POST then proccess data
	if request.method == 'POST':
        # Create 2 form instances and populate them with data from the POST request
		form1 = SignUpForm(request.POST)
        # Check whether it's valid
		if form1.is_valid():
			# Save main user form first and hash password
			try:
				user = form1.save(commit=False)
				user.set_password(user.password)
				user.save()
				# Change sign up flag to true
				signedUp = True
				return HttpResponse("Your account is registered.")
			except:
				signedUp = False
		else:
			return HttpResponse("Your account is not registered.")
    # If request is not POST create empty forms
	else:
		#form1 = SignUpForm()
		template = loader.get_template('Propylaea/login_register.html')
		context = {
			'SignUpForm': SignUpForm,
			'LoginForm': LoginForm,
		}
		return HttpResponse(template.render(context, request))
		#return HttpResponseRedirect('/Eisegesis/Eisegesis')
		#return render(request, 'Propylaea/login_register.html', {'SignUpForm': SignUpForm, 'LoginForm': LoginForm})

def LogIn(request):
	# If the request is type of POST then proccess data
	if request.method == 'POST':
		#forml = LoginForm(request.POST)
		#if forml.is_valid():
		#email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		#email = request.POST['email']
		#password = request.POST['password']
		# Authenticate
		#user = authenticate(email=email, password=password)
		user = authenticate(username=username, password=password)
		# User valid
		if user is not None:
			if user.is_active:
				login(request, user)
				#return HttpResponse("Your account is logged in.")
				return HttpResponseRedirect('/eisegesis/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			return HttpResponse("Invalid login details supplied")#: {0}, {1}".format(email, password))
	else:
		template = loader.get_template('Propylaea/login_register.html')
		context = {
			'LoginForm': LoginForm,
			'SignUpForm': SignUpForm,
		}
		return HttpResponse(template.render(context, request))
		#return render_to_response('Propylaea/login_register.html', {}, context)

@login_required
def UsrLogout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/user/login/')
