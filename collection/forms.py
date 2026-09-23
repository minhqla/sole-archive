from django import forms
from .models import CollectionItem, Sneaker


class CollectionItemForm(forms.ModelForm):
    class Meta:
        model = CollectionItem
        # We leave out 'user' because we will set that automatically
        # in the view based on who is logged in
        fields = ['sneaker', 'size', 'condition', 'status', 'price_paid', 'purchase_date', 'is_favourite', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SneakerForm(forms.ModelForm):
    class Meta:
        model = Sneaker
        fields = ['brand', 'silhouette', 'colorway', 'release_date', 'retail_price', 'image']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
