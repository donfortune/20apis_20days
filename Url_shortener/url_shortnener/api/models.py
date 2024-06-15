from django.db import models
import string
import random

# Create your models here.
class urlModel(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
    
