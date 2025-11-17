from django.contrib import admin

# Register your models here.
from .models import Course ,Subject

admin.site.register(Course)
admin.site.register(Subject)