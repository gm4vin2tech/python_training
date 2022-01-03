from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def que(request):
	# return HttpResponse("This is question paper")

def que(request):
	return render(request, "base.html", {"name": 'gowthami'})	