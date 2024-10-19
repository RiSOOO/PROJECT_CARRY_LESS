from django.urls import reverse
from django.test import TestCase
from viewer.models import Product


class ProductTest(TestCase):
    def setUp(self):
        # Vytvoření testovacího produktu
        Product.objects.create(name="Test product", price=10, weight=1, brand="Test brand", category_ID=1)

    def test_product(self):
        # Test, že vytvořený produkt má správnou cenu
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.price, 10)

    def test_product_category(self):
        # Test, že vytvořený produkt ma správnou kategorii
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.category_ID, 1)

    def test_product_brand(self):
        # Test, že vytvořený produkt ma správnou značkou
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.brand, "Test brand")

    def test_product_weight(self):
        # Test, že vytvořený produkt ma správnou hmotnost
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.weight, 1)

    def test_product_name(self):
        # Test, že vytvořený produkt ma správné jméno
        product = Product.objects.get(name="Test product")
        self.assertEqual(product.name, "Test product")

