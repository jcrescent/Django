from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'ninja_app/index.html')

def show_all(request):
	return render(request, 'ninja_app/ninja.html')

def show_specific(request, color):
	if color == "blue":
		turtle = 'leonardo.jpg'
	elif color == "red":
		turtle = 'raphael.jpg'
	elif color == "purple":
		turtle = 'donatello.jpg'
	elif color == "orange":
		turtle = 'michelangelo.jpg'
	else:
		turtle ='megan.png'
	print turtle
			
	context = {
		'turtle': turtle
	}
	return render(request, 'ninja_app/turtle.html', context)


