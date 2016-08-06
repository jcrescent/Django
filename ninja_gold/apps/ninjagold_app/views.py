from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime

# Create your views here.
def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'log' in request.session:
		request.session['log'] = ''	
		return render(request, 'ninjagold_app/index.html')
	else:
		message = request.session['log']
		context = {'message' : message}
		return render(request, 'ninjagold_app/index.html', context)


def process_gold(request):
	def getGoldFrom(name, min, max):
		loot = random.randint(min, max)
		time = strftime("%b %d, %Y %I: %M %p") 
		request.session['gold'] += loot
		if loot > 0:
			request.session['log'] += "<p style='color:green;'>You got "+str(loot)+" gold from the "+str(name)+"! ["+str(time)+"]</p>"
		else:
			request.session['log'] += "<p style='color:red;'>You got "+str(loot)+" gold from the "+str(name)+"! ["+str(time)+"]</p>"
	if request.GET['place'] == "Go to the farm":
			getGoldFrom('farm', 10 , 20)
	if request.GET['place'] == "Go to the cave":
			getGoldFrom('cave', 5, 10)
	if request.GET['place'] == "Go to the house":
			getGoldFrom('house', 2, 5)
	if request.GET['place'] == "Go to the casino":
			getGoldFrom('casino', -50, 50)
	return redirect('/')	