"""Carry_less URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from viewer.models import Categorie
from viewer.models import Product, CartItem
from viewer.models import ProductFeature
from viewer.views import MainPageView, CategoriesView, ProductsView, ProductsCreateView
from viewer.views import ProductsUpdateView, ProductsDeleteView, UserView, SignUpView
from viewer.views import ProductList, ViewCart

admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(ProductFeature)
admin.site.register(CartItem)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
    path('eshop/', MainPageView.as_view(), name='main'),
    path('kategorie/', CategoriesView.as_view(), name='kategorie'),
    path('', MainPageView.as_view(), name='main'),
    path('eshop/', MainPageView.as_view(), name='main'),
    path('produkty/', ProductsView.as_view(), name='produkty'),
    path('accounts/', include('accounts.urls')),
    path('produkty/create/', ProductsCreateView.as_view(), name='create_product'),
    path('produkty/update/<int:pk>/', ProductsUpdateView.as_view(), name='update_product'),
    path('produkty/delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_product'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('userpage/', UserView.as_view(), name='userpage'),
    path('accounts/register/', SignUpView.as_view(), name='registration'),


    path('products/', ProductList.as_view(), name='product_list'),
    path('cart/', ViewCart.as_view(), name='view_cart')


]
