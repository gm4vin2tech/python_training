from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("The home page")


def demo(request):
	return render(request, "base.html")	