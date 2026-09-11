from django.db import models
from django.contrib.auth.models import User


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


class CollectionItem(models.Model):
    # This links a User to a Sneaker they own (or want)
    CONDITION_CHOICES = [
        ('new', 'Brand New'),
        ('used', 'Used'),
    ]

    STATUS_CHOICES = [
        ('owned', 'Owned'),
        ('wishlist', 'Wishlist'),
    ]

    # UK shoe sizes - full and half sizes only
    UK_SIZE_CHOICES = [
        ('3', 'UK 3'), ('3.5', 'UK 3.5'),
        ('4', 'UK 4'), ('4.5', 'UK 4.5'),
        ('5', 'UK 5'), ('5.5', 'UK 5.5'),
        ('6', 'UK 6'), ('6.5', 'UK 6.5'),
        ('7', 'UK 7'), ('7.5', 'UK 7.5'),
        ('8', 'UK 8'), ('8.5', 'UK 8.5'),
        ('9', 'UK 9'), ('9.5', 'UK 9.5'),
        ('10', 'UK 10'), ('10.5', 'UK 10.5'),
        ('11', 'UK 11'), ('11.5', 'UK 11.5'),
        ('12', 'UK 12'), ('12.5', 'UK 12.5'),
        ('13', 'UK 13'), ('13.5', 'UK 13.5'),
        ('14', 'UK 14'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    size = models.CharField(max_length=4, choices=UK_SIZE_CHOICES)  # UK size
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='new')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='owned')
    price_paid = models.PositiveIntegerField(blank=True, null=True)  # whole pounds (£), no pence
    purchase_date = models.DateField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + str(self.sneaker)