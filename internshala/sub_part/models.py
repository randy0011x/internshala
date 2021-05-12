from django.db import models
from multiselectfield import *


# Create your models here.
class add_new_menu(models.Model):
    Pizzaname = models.CharField(max_length=20)

    # Foodtype = models.CharField(max_length=4)
    # Foodsize = models.CharField(max_length=10)
    # Pizzaprice = models.CharField(max_length=10)

    def __str__(self):
        return self.Pizzaname


class menuorder(models.Model):
    Pizzaorder = models.CharField(max_length=20)
    Foodtype = models.CharField(max_length=4)
    Foodsize = models.CharField(max_length=10)
    Topping_choices = (
        ('Onion', 'Onion'),
        ('Tomato', 'Tomato'),
        ('Corn', 'Corn'),
        ('Cheese', 'Cheese'),
        ('Capsicum', 'Capsicum'),
        ('Jalapeno', 'Jalapeno'),
    )
    Toppings = MultiSelectField(choices=Topping_choices)

    def __str__(self):
        return self.Foodtype



