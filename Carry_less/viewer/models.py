from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"Kategorie {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.IntegerField()
    brand = models.CharField(max_length=300)
    category_ID = models.IntegerField()

    def __str__(self):
        return (f"Nabídka {self.name} - {self.weight} - {self.price} - {self.brand} -{self.category_ID}")
