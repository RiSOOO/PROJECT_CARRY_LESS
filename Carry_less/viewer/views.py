from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm

from viewer.models import Categorie
from viewer.models import Product

class MainPageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    "all_categories": Categorie.objects.all(),
    "all_products": Product.objects.all()

    }

class CategoriesView(TemplateView):
    template_name = "kategorie.html"
    extra_context = {
    "all_categories" : Categorie.objects.all()

    }

class ProductsView(TemplateView):
    template_name = "produkty.html"
    extra_context = {
    "all_products": Product.objects.all()

    }


