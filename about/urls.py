from django.urls import path
from .views import About, cv

app_name="about"
urlpatterns = [
	path('', About.as_view(), name='about'),
	path('cv/', cv, name='cv'),
]