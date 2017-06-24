from django.contrib import admin

from .models import Post, Settings

admin.site.register(Post)
admin.site.register(Settings)

# Register your models here.
