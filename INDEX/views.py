from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'INDEX/index.html')

def exit(request):
	return render(request, 'INDEX/exit.html')