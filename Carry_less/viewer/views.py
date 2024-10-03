from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm

from viewer.models import Categorie
from viewer.models import Product

from django.urls import reverse_lazy
from viewer.forms import ProductsForm

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

class ProductsCreateView(LoginRequiredMixin,CreateView):
  template_name = 'form.html'
  model = Product
  form_class = ProductsForm
  success_url = reverse_lazy("produkty")

class ProductsUpdateView(PermissionRequiredMixin, UpdateView):
  template_name = 'form.html'
  model = Product
  form_class = ProductsForm
  success_url = reverse_lazy("produkty")
  permission_required = 'viewer.change_product'

class ProductsDeleteView(PermissionRequiredMixin, DeleteView):
  template_name = 'product_confirm_delete.html'
  model = Product
  success_url = reverse_lazy("produkty")
  permission_required = 'viewer.delete_product'

class UserView(TemplateView):
  template_name = "user.html"







