# models.py
from importlib.resources import contents
from django.utils import timezone
from django.db import models

class Post(models.Model):
    def __init__(self,title,content,pk):
        super().__init__()
        self.title = title
        self.content = content
        self.published_at = timezone.now()
        self.pk=pk
    def __str__(self):
        return self.title