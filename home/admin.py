from django.contrib import admin
from .models import BlogModel, Profile

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(Profile)
