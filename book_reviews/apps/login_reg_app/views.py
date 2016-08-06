from django.shortcuts import render, redirect, HttpResponse
from .models import Users

def index(request):
	return render(request, 'login_reg_app/index.html')

def register(request):
	reg_try = Users.usersManager.validation(request.POST)
	if reg_try['successful']:
		request.session['name'] = reg_try['user'].first_name
		request.session['id'] = reg_try['user'].id
		context = {'message': "registered!"}
		return render(request, 'login_reg_app/success.html', context)
	else:
		messages = reg_try['invalids']
		context = {'messages': messages}
		return render(request, 'login_reg_app/index.html', context)
			
def login(request):
	login_try = Users.usersManager.login_val(request.POST)
	if login_try['successful']:
		request.session['name'] = login_try['user'].first_name
		request.session['id'] = login_try['user'].id
		context = {'message': 'logged in!'}
		return render(request, 'login_reg_app/success.html', context)
	else:
		context = {'message': "Incorrect email or password"}
		return render(request, 'login_reg_app/index.html', context)