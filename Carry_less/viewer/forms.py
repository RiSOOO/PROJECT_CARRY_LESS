from django.core.exceptions import ValidationError
from django.forms import ModelForm
from viewer.models import Product

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        if len(self.cleaned_data["name"]) < 3:
            raise ValidationError("název je moc krátký")
        if Product.objects.filter(name=self.cleaned_data["name"]).exists():
            raise ValidationError("produkt s tímto názvem již existuje")
        return self.cleaned_data["name"]

    def clean_price(self):
        if self.cleaned_data["price"] > 0:
            return self.cleaned_data["price"]
        raise ValidationError("cena musí být větší než nula")



     

