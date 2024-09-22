from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return f"Kategorie {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=70)
    weight = models.IntegerField()
    price = models.IntegerField()
    brand = models.CharField(max_length=70)
    category_ID = models.IntegerField()
    products_of_categories = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return (f" Produkt {self.name} , {self.weight} , {self.price} , {self.brand} , {self.category_ID} , {self.products_of_categories}")
