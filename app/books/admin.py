from django.contrib import admin

from .models import Profile, Book, Comment

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Comment)