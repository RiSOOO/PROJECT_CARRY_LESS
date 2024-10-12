from django.forms import ModelForm
from viewer.models import Product

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
