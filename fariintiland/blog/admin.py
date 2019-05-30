from django.contrib import admin

# Register your models here.

from . import models
# from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
                        'slug',
                        'waktu_posting',
                        'waktu_update',
                        ]

admin.site.register(models.Post, PostAdmin)
