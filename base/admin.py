from django.contrib import admin
from .models import contact

# Register your models here.
class AdminContact(admin.ModelAdmin):
	list_display = ['address', 'phone_number', 'email', 'my_id']


admin.site.register(contact, AdminContact)