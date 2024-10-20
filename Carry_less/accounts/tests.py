#from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserLoginTest(LiveServerTestCase):
    def setUp(self):
        # Vytvoření testovacího uživatele
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get(f'{self.live_server_url}/accounts/login/')

        # Najít pole pro zadání uživatelského jména a hesla
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')

        # Vyplnit formulář přihlášení
        username_input.send_keys('testuser')
        password_input.send_keys('12345')

        # Odeslat formulář
        password_input.send_keys(Keys.RETURN)

        # Ověřit, zda přihlášení proběhlo úspěšně (např. přesměrování na domovskou stránku)
        self.assertIn('Vítejte na eshopu Carry less!', self.driver.page_source)
