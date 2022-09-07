from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'language_type', 'publish', 'statuc']
	list_filter  =['language_type', 'statuc', 'publish'] 
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-publish']
	search_fields = ('title', 'description')

admin.site.register(Project, ProjectAdmin)