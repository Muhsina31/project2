from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # The form is based on the Product model
        fields = ['productname', 'image', 'price', 'details']  # Fields to be displayed in the form
        widgets = {
            'productname': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }
