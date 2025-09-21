from django.contrib import admin

# Register your models here.

# assets/admin.py
from django.contrib import admin
from .models import Category, Asset

admin.site.register(Category)
admin.site.register(Asset)