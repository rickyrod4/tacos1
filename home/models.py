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
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
<<<<<<< HEAD
    ordered_by = models.ForeignKey(User, related_name='tacos_ordered', on_delete=models.CASCADE, null = True)
=======
    ordered_by = models.ForeignKey(User, related_name='tacos_ordered', on_delete=models.CASCADE, default = None)
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class Taco(models.Model):
    #ingredients - Ingredient(model)
    tortilla_choices = [
        ('flour', 'Flour'),
        ('corn', 'Corn'),
    ]
    tortilla = models.CharField(max_length = 10, choices = tortilla_choices, default = 'flour')
    taco_price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity_ordered = models.IntegerField()

<<<<<<< HEAD
    order = models.ForeignKey(Order, related_name='tacos_on_order', on_delete=models.CASCADE, null = True)
=======
    order = models.ForeignKey(Order, related_name='tacos_on_order', on_delete=models.CASCADE)
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Ingredient(models.Model):
    ingredient_choices = [
        ('egg', 'Egg'),
        ('potato', 'Potato'),
        ('bean', 'Bean'),
        ('cheese', 'Cheese'),
        ('carne asada', 'Carne Asada'),
        ('chicken fajita', 'Chicken Fajita'),
        ('beef fajita', 'Beef Fajita'),
        ('pastor', 'Pastor'),
        ('barbacoa', 'Barbacoa'),
        ('lengua', 'Lengua'),
        ('bacon', 'Nacon'),
        ('nopales', 'Nopales'),
        ('sausage', 'Sausage'),
    ]

    ingredient = models.CharField(max_length = 255, choices = ingredient_choices)
    ingredient_price = models.DecimalField(decimal_places=2, max_digits=5)
<<<<<<< HEAD
    taco = models.ForeignKey(Taco, related_name='ingredients', on_delete=models.CASCADE, null = True)
=======
    taco = models.ForeignKey(Taco, related_name='ingredients', on_delete=models.CASCADE)
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
<<<<<<< HEAD
        return self.ingredient
=======
        return self.ingredient + ' $' + self.ingredient_price
>>>>>>> 43999b2f992eea9c46e7bb4d1feaca9110a228cc
    




