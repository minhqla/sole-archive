from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sneaker(models.Model):
    # This is the "catalog" info about a shoe - not tied to one user
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    silhouette = models.CharField(max_length=150)  # e.g. "Air Max 90"
    colorway = models.CharField(max_length=150)    # e.g. "Triple Black"
    release_date = models.DateField(blank=True, null=True)
    retail_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='sneakers/', blank=True, null=True)

    def __str__(self):
        return self.brand.name + " " + self.silhouette + " - " + self.colorway