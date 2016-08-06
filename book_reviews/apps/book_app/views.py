from django.shortcuts import render

def home(request):

	return render(request, 'book_app/home.html')

def add(request):
	return render(request, 'book_app/new.html')

def create(request):
	return redirect('/')

		
