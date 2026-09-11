from django.contrib import admin
from .models import Brand, Sneaker, CollectionItem

# Register your models here.

admin.site.register(Brand)
admin.site.register(Sneaker)
admin.site.register(CollectionItem)