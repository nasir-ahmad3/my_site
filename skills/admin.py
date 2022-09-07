from django.contrib import admin
from .models import Skill

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
	list_display = ['title', 'learn_presentage']
	list_filter= ('learn_presentage',)
	search_fields = ('title', 'learn_presentage')
	ordering = ('learn_presentage',)
admin.site.register(Skill, SkillAdmin)