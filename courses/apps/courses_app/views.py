from django.shortcuts import render, HttpResponse, redirect
from .models import Courses

# Create your views here.
def index(request):
	courses = Courses.objects.all()
	context = {
		'courses': courses
	}
	return render(request, 'courses_app/index.html', context)

def create(request):
	Courses.objects.create(name = request.POST['name'], description = request.POST['description']) 
	return redirect('/')

def show(request, id):
	course = Courses.objects.get(id = id)
	context = {
		'course' : course
	}
	print context
	return render(request, 'courses_app/delete.html', context)

def delete(request, id):
	Courses.objects.get(id=id).delete()
	
	return redirect ('/')	

def back(request):
	return redirect('/')	