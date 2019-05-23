from django.contrib import admin

# Register your models here.

from . import models
# from .models import Post
admin.site.register(models.Post)
