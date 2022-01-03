from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("This is my first page")

def demo(request):
	return HttpResponse("This is my second page")

