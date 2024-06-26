from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import django_filters

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    


    def __str__(self):
        return f'{self.user.username} Profile'
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('leisure', 'Leisure'),
        ('electronics', 'Electronics'),
        ('utilities', 'Utilities'),
        ('clothing', 'Clothing'),
        ('health', 'Health'),
        ('others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity}'
    
