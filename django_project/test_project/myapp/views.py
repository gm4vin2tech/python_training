from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime
from .models import Destination
def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   # return HttpResponse(text)
   # return render(request, "hello.html")
   # return render(request, "hello.html", {})
   # return render(request, "hello.html", {'name': 'Gowthami Manjunatha', 'number': 'number'})
   today = datetime.now().date()
   # return render(request, "hello.html", {"today" : today})
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def head(request):
   return render(request, "head.html")

def add(request):
   num1 = request.POST["num1"]
   num2 = request.POST["num2"]
   result = int(num1) + int(num2)
   return render(request, "result.html",{'result': result})

def index(request):
	dests = Destination.objects.all()
	return render(request, "index.html", {'dests': dests})   



