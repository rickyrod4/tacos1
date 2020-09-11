from django.db import models
from django import forms
from django.forms import ModelForm 
from .forms import SignUpForm
from django.contrib.auth.models import User
import re

#Email Regex101
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Taco(models.Model):
    taco_type = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    tacos_for = models.ForeignKey(User, related_name='taco_history', on_delete=models.CASCADE)
    favorite = models.ForeignKey(User, related_name='favorite_taco', on_delete=models.CASCADE, default = None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    ordered_by = models.ForeignKey(User, related_name='tacos_ordered', on_delete=models.CASCADE, default = None)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 