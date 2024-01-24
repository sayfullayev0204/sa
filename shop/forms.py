from django import forms
from .models import Product
from .models import Category
class ProductForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"Enter your product name"}), label="Product Name")

        model = Product
        fields = ['Turi','Ismingiz', 'nomi','malumoti','narxi','rasmi','ulanish']
