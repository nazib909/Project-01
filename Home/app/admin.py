from django.contrib import admin
from .models import userProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fields=['user','gender','phone','address','birthday','image']
admin.site.register(userProfile)