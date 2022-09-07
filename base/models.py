from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class contact(models.Model):
	address 		= models.CharField(max_length=500)
	phone_number 	= PhoneNumberField() 
	email  			= models.EmailField(max_length=200)
	my_id 			= models.IntegerField(help_text='to show the model in the page please take the my_id to 1')