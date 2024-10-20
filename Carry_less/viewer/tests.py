from django.urls import reverse
from django.test import TestCase
from viewer.models import Product, CartItem, User
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

# selenium test -
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By



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


class CartTest(TestCase):
    def setUp(self):
        # Vytvoření testovacího uživatele
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Vytvoření testovacích produktů
        self.product1 = Product.objects.create(name="Product 1", price=10, weight=1, brand="Brand 1", category_ID=1)
        self.product2 = Product.objects.create(name="Product 2", price=20, weight=2, brand="Brand 2", category_ID=2)

    def test_add_to_cart(self):
        # Přidání produktu do košíku
        CartItem.objects.create(user=self.user, product=self.product1, quantity=2)

        # Ověření, že produkt je v košíku s požadovaným množstvím
        cart_item = CartItem.objects.get(user=self.user, product=self.product1)
        self.assertEqual(cart_item.quantity, 2)

    def test_cart_total_price(self):
        # Přidání produktů do košíku
        CartItem.objects.create(user=self.user, product=self.product1, quantity=2)  # 2x produkt1 (2 * 10)
        CartItem.objects.create(user=self.user, product=self.product2, quantity=1)  # 1x produkt2 (1 * 20)

        # Výpočet celkové ceny košíku
        cart_items = CartItem.objects.filter(user=self.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Ověření celkové ceny
        self.assertEqual(total_price, 40)

    def test_remove_from_cart(self):
        # Přidání produktu do košíku
        cart_item = CartItem.objects.create(user=self.user, product=self.product1, quantity=2)

        # Odebrání produktu z košíku
        cart_item.delete()

        # Ověření, že produkt byl odstraněn
        cart_items = CartItem.objects.filter(user=self.user, product=self.product1)
        self.assertEqual(cart_items.count(), 0)

    def test_cart_empty(self):
        # Ověření, že košík je prázdný na začátku
        cart_items = CartItem.objects.filter(user=self.user)
        self.assertEqual(cart_items.count(), 0)



class MySeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up the WebDriver for Safari
        cls.selenium = webdriver.Safari()  # Change to Safari WebDriver
        cls.selenium.implicitly_wait(10)
        cls.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # Access the live server URL
        self.selenium.get(f'{self.live_server_url}/accounts/login/')
        # Find the username and password input fields and fill them
        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        username_input.send_keys('admin')
        password_input.send_keys('admin')
        # Submit the form
        self.selenium.find_element(By.XPATH, '//input[@type="submit"]').click()
        import time
        time.sleep(2)
        # Test that we successfully logged in (check for a successful redirect or message)
        self.assertIn("Uživatel: admin", self.selenium.page_source)