from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project
from django.http import HttpResponse

# Create your views here.
class ProjectList(ListView):
	queryset = Project.objects.published()
	context_object_name = 'projec_list'


class ProjectDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Project.objects.published(), slug=slug)
