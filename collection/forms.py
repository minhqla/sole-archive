from django import forms
from .models import CollectionItem, Sneaker


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'maxlength': 20}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 20:
            raise forms.ValidationError('Username must be 20 characters or fewer.')
        return username

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
