from django.contrib import admin

from .models import Category, Lectures

# Register your models here.
admin.site.register(Category)
admin.site.register(Lectures)

admin.site.site_header = "Medical Tutorial Room"
admin.site.site_title = "Medical Tutorial Room"
admin.site.index_title = "Welcome to Medical Tutorial Room"
