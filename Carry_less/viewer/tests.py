from django.urls import reverse
from django.test import TestCase
from viewer.models import Product


class ProductTest(TestCase):
    def setUp(self):
        # Vytvoření testovacího produktu
        Product.objects.create(name="Test product", price=10)

    def test_product(self):
        # Test, že vytvořený produkt má správnou cenu
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.price, 10)
