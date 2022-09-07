from django.shortcuts import render
from django.views.generic import ListView
from .models import Skill

# Create your views here.
class SkillList(ListView):
	model = Skill
	context_object_name = 'skill_list'