from django import forms
from allauth.account.forms import SignupForm as AllauthSignupForm
from .models import CollectionItem, Sneaker


class CustomSignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 20
        self.fields['username'].help_text = (
            'Required. 20 characters or fewer. '
            'Letters, digits and @/./+/-/_ only.'
        )

    def clean_username(self):
        username = super().clean_username()
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

from django import forms
from allauth.account.forms import SignupForm as AllauthSignupForm
from .models import CollectionItem, Sneaker


class CustomSignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 20
        self.fields['username'].help_text = 'Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'

    def clean_username(self):
        username = super().clean_username()  # keep allauth's own checks (e.g. uniqueness)
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


class CollectionItemDetailsForm(forms.ModelForm):
    """
    Same as CollectionItemForm but without the 'sneaker' field - used when
    creating a brand new sneaker and adding it to the collection at the same time.
    """
    class Meta:
        model = CollectionItem
        fields = ['size', 'condition', 'status', 'price_paid', 'purchase_date', 'is_favourite', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }