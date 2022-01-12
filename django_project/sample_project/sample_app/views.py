from django.shortcuts import render
from sample_app.models import Destination
# Create your views here.

from django.http import HttpResponse
from datetime import datetime
def hello(request):
	return render(request, 'base.html')

def index(request):
	dests = Destination.objects.all()
	return render(request, 'index.html', {'dests': dests})

def add(request):
	num1 = request.POST['num1']
	num2 = request.POST['num2']
	result = int(num1) + int(num2)
	return render(request, 'result.html', {'result': result})

