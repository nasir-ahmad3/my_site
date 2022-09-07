from django.urls import path
from .views import ProjectList, ProjectDetail

app_name= 'projects'
urlpatterns = [
	path('', ProjectList.as_view(), name='ProjectList'),
	path('detail/<slug:slug>', ProjectDetail.as_view(), name='ProjectDetail'),
]

