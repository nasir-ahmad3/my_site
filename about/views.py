from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import About

# Create your views here.

class About (ListView):
	model = About
	context_object_name = 'about_list'

def cv(request):
	return render(request, 'about/cv.html')