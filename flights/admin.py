from django.contrib import admin
from .models import flight,airport
# Register your models here.
admin.site.register(airport)
admin.site.register(flight)