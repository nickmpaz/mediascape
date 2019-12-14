from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self): 
        
        return self.title

class Comment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):

        return self.text[:50]