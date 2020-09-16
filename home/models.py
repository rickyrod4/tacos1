from django.db import models
from django import forms
from django.forms import ModelForm 
from .forms import SignUpForm
from django.contrib.auth.models import User
import re

#Email Regex101
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Order(models.Model):
    #tacos_on_order - Taco(model)
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    ordered_by = models.ForeignKey(User, related_name='tacos_ordered', on_delete=models.CASCADE, default = None)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class Taco(models.Model):
    #ingredients - Ingredient(model)
    tortilla_choices = [
        ('flour'),
        ('corn'),
    ]
    tortilla = models.CharField(max_length = 10, choices = tortilla_choices, default = 'flour')
    taco_price = models.DecimalField(decimal_places=2, max_digits=5)

    order = models.ForeignKey(Order, related_name='tacos_on_order', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Ingredient(models.Model):
    ingredient_choices = [
        ('egg'),
        ('potato'),
        ('bean'),
        ('cheese'),
        ('carne asada'),
        ('chicken fajita'),
        ('beef fajita'),
        ('pastor'),
        ('barbacoa'),
        ('lengua'),
        ('bacon'),
        ('nopales'),
        ('sausage'),
    ]

    ingredient = models.CharField(max_length = 255, choices = ingredient_choices)
    ingredient_price = models.DecimalField(decimal_places=2, max_digits=5)
    taco = models.ForeignKey(Taco, related_name='ingredients', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.ingredient + ' $' + self.ingredient_price
    




