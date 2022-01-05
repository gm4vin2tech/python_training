from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime
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



