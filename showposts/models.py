# models.py
from importlib.resources import contents
from django.utils import timezone
from django import forms
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,default='papiez')
    content = models.TextField(default="")
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Specify which fields you want in the form