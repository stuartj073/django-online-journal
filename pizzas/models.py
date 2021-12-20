from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.Charfield(max_length=15)

    def __str__(self):
        """ Return a string representation of the model """
        return self.name


class Toppings(models.Model):
    pizza = modles.ForeignKey(Pizza, on_delete=models.CASCADE)