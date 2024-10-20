# PROJECT_CARRY_LESS
 On-line obchod s turistickým zbožím.

1. Nainstalujte Python a Django
Nejdříve potřebujete mít nainstalovaný Phycharm a Django.

a) Instalace Phycharm:
Pokud ještě nemáte Phycharm nainstalován, stáhněte si ho z oficiálních stránek . Ujistěte se, že máte verzi 3.12.

b) Instalace Django:
Po instalaci Pythonu můžete nainstalovat Django pomocí příkazu:

bash
"pip install django"
Tento příkaz nainstaluje aktuální verzi Djanga.

2. Vytvoření Django projektu
Django projekt je základní struktura, kde budete umisťovat svou aplikaci. Pro vytvoření projektu použijte tento příkaz:

bash
"django-admin startproject carry_less_project"
Tímto příkazem vytvoříte nový projekt s názvem CARRY_LESS_PROJECT.

Přejděte do složky projektu:

bash
"cd carry_less_project"

3. Vytvoření Django aplikace
Nyní vytvoříme vlastní aplikaci, kterou pojmenujeme například carry_less. To se provádí následujícím příkazem:

bash
"python manage.py startapp carry_less"
Tímto příkazem se vytvoří složka carry_less, kde bude aplikace umístěna.

4. Nastavení aplikace v projektu
Django aplikace musí být zaregistrována v souboru settings.py, který najdete ve složce carry_less_project. Otevřete soubor settings.py a přidejte carry_less do seznamu INSTALLED_APPS:

phycharm
"carry_less_project/settings.py"

INSTALLED_APPS = [
    # Django default apps...
    'carry_less',
]

5. Nastavení databáze
Django standardně používá SQLite, která nevyžaduje žádnou další konfiguraci. Pokud potřebujete používat jinou databázi (např. PostgreSQL nebo MySQL), upravte DATABASES v souboru settings.py.

Poté můžete vytvořit databázové tabulky pomocí příkazu:

bash
"python manage.py migrate"
Tímto příkazem se nastaví základní struktura databáze.

6. Vytvoření základní struktury aplikace
Nyní můžete začít vytvářet pohledy (views), URL, šablony a modely pro aplikaci carry_less.

a) URL routing:
Vytvořte soubor urls.py ve složce aplikace carry_less a definujte základní URL:

phycharm
"carry_less/urls.py"

from django.urls import path
from viewer import views

urlpatterns = [
    path('', views.index, name='index'),
]
Poté přidejte tento soubor do hlavního souboru urls.py v projektu:

phycharm
"carry_less/urls.py"

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

b) Pohledy (views):
V souboru views.py vytvořte základní pohled:

phycharm
"carry_less/views.py"

from django.shortcuts import render

def index(request):
    return render(request, 'carry_less/index.html')

c) Šablony (templates):

Vytvořte složku templates v aplikaci carry_less a v ní složku carry_less. Zde vytvořte soubor index.html:

markdown
carry_less/
    templates/
            index.html
V souboru index.html můžete přidat základní HTML kód, například:

index.html

<!DOCTYPE html>
<html>
<head>
    <title>Carry_less</title>
</head>
<body>
    <h1>Vítejte na eshopu Carry less!</h1>
    <p>Zde můžete pořídit vše na kempování.</p>
</body>
</html>

7. Spuštění vývojového serveru
Nyní je aplikace připravena a můžete ji spustit na vývojovém serveru. Použijte příkaz:

bash
"python manage.py runserver"
Po zadání adresy http://127.0.0.1:8000/ do prohlížeče byste měli vidět svou aplikaci Carry_less.

8. Další kroky
Teď, když aplikace běží, můžete pokračovat v jejím rozvoji:

Přidávejte další URL, pohledy a šablony.
Vytvářejte modely pro databázové tabulky.
Přidávejte formuláře, autentizaci uživatelů a další funkce.
Toto je základní průvodce instalací a rozběhnutím Django aplikace Carry_less.

- [x] Nápad na eshop a jeho sortiment, tvorba loga<br>
- [x] Tvorba E-R diagramu <br>
 - [x] Vytvoření základní šablony webu v Django<br>
- [x] Vytvoření kategorií produktů<br>
 - [x] Přidání konkrétních produktů<br>
 - [x] Vytvořit admina<br>
 - [x] Vytvořit uživatele<br>
 - [x] Definovat oprávnění admin/uživatel<br>
 - [x] Přidat další kategorie<br>
 - [ ] Vytvořit strom kategorií<br>
 - [x] Design<br>
 - [x] validace vstupních dat
