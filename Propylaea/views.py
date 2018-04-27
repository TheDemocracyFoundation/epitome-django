from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Propylaea.forms import LoginForm, SignUpForm
from django.template import loader
from django.contrib.auth.decorators import login_required

def SignUpV(request):
	signedUp = False					# Signed up flag
	if request.method == 'POST':		# If the request is type of POST then proccess data
		form1 = SignUpForm(request.POST)# Create 2 form instances and populate them with data from the POST request
		if form1.is_valid():			# Check whether it's valid
			try:						# Save main user form first and hash password
				user = form1.save(commit=False)
				user.set_password(user.password)
				user.save()				# Change sign up flag to true
				signedUp = True
				return HttpResponseRedirect('/demoscopesis/')
			except:
				signedUp = False
		else:
			template = loader.get_template('error.html')
			context = {
				"errorType": "409",
				"errorMessage": "Your prefered credentials were received but your account was not created. Please try again with a different username.",
				"redirectTo": "/user/signup"
			}
			return HttpResponse(template.render(context, request))
	else:								# If request is not POST create empty forms
		#form1 = SignUpForm()
		template = loader.get_template('Propylaea/login.html')
		context = {
			'SignUpForm': SignUpForm,
			'LoginForm': LoginForm,
		}
		return HttpResponse(template.render(context, request))
		#return HttpResponseRedirect('/Eisegesis/Eisegesis')
		#return render(request, 'Propylaea/login_register.html', {'SignUpForm': SignUpForm, 'LoginForm': LoginForm})

def LogIn(request):
	if request.method == 'POST':				# If the request is type of POST then proccess data
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
		if user is not None:					# User valid
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/demoscopesis/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			#return HttpResponse("Invalid login details supplied")#: {0}, {1}".format(email, password))
			template = loader.get_template('error.html')
			context = {
				"errorType": "401",
				"errorMessage": "You are not authorized to login. Please check your credentials or register an account",
				"redirectTo": "/user/login"
			}
		return HttpResponse(template.render(context, request))
	
	else:
		template = loader.get_template('Propylaea/login.html')
		context = {
			'LoginForm': LoginForm,
			'SignUpForm': SignUpForm,
		}
		return HttpResponse(template.render(context, request))
		#return render_to_response('Propylaea/login_register.html', {}, context)
				

@login_required(login_url='/user/login/')
def UsrLogout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/user/login/')
