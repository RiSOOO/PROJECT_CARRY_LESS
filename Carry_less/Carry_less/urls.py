"""Carry_less URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from viewer.views import MainPageView, CategoriesView, ProductsView, AuthenticationForm, ProductsCreateView, ProductsUpdateView

from viewer.models import Categorie
from viewer.models import Product

admin.site.register(Categorie)
admin.site.register(Product)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
    path('eshop/', MainPageView.as_view(), name='main'),
    path('kategorie/', CategoriesView.as_view(), name='kategorie'),
    path('', MainPageView.as_view(), name='main'),
    path('eshop/', MainPageView.as_view(), name='main'),
    path('kategorie/', CategoriesView.as_view(), name='kategorie'),
    path('produkty/', ProductsView.as_view(), name='produkty'),
    path('accounts/', include('accounts.urls')),
    path('produkty/create/', ProductsCreateView.as_view(), name='create_product'),
    path('produkty/update/<int:pk>/', ProductsUpdateView.as_view(), name='update_product')



]
