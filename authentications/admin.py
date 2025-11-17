from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,OTP, UserProfile
#register customuser

admin.site.register(CustomUser)
admin.site.register(UserProfile)

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('email','otp','create_at','attempts')
    list_filter = ('create_at',)
    search_fields = ('email','otp')