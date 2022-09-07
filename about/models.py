from django.db import models 
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class About(models.Model):
	name 			= models.CharField(max_length=200)
	pictuer 		= models.ImageField(upload_to="my_pictuer")
	job 			= models.CharField(max_length=30)
	about_my_self 	= models.TextField()

	def show_pictuer(self):
		return format_html('<img style="width:100px; height: 100px; border-radius:50%;" src="{}">'.format(self.pictuer.url))
