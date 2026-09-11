from django import forms
from .models import CollectionItem


class CollectionItemForm(forms.ModelForm):
    class Meta:
        model = CollectionItem
        # We leave out 'user' because we will set that automatically
        # in the view based on who is logged in
        fields = ['sneaker', 'size', 'condition', 'status', 'price_paid', 'purchase_date', 'is_favorite', 'notes']