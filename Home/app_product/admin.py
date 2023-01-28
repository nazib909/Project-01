from django.contrib import admin
from .models import Category,Products

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields=['c_name']
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    fields=['p_name','price','p_price','description','quantity','p_pic','Category']
admin.site.register(Products)