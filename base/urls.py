from django.urls import path
from .views import home, ContactSuccessView

app_name ="base"
urlpatterns = [
	path('', home, name="home"),
	path('success/', ContactSuccessView.as_view(), name="success"),
]