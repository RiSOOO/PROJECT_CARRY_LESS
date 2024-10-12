from django.contrib.auth.forms import (UserCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from viewer.forms import ProductsForm
from viewer.models import Categorie
from viewer.models import Product
from viewer.models import CartItem
from django.contrib.auth.models import User


class MainPageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    "all_categories": Categorie.objects.all(),
    "all_products": Product.objects.all()

    }

class CategoriesView(TemplateView):
    def get(self,request,*args,**kwargs):
        category_id=request.GET.get("id")

        if(category_id==None):
            extra_context = {
                "all_categories": Categorie.objects.all()
            }
        else:
            extra_context={
                "category": Categorie.objects.get(id=category_id),
                "products": Product.objects.filter(products_of_categories=category_id)
            }
        return render(request,"kategorie.html",extra_context)

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

class SignUpView(CreateView):
  template_name = 'form.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('login')



class ProductList(TemplateView):
    products = Product.objects.all()
    template_name = "producst_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Zde přidáme seznam produktů do kontextu
        return context


class ViewCart(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.request.session.get('cart', [])
        context['cart_items'] = cart_items

        # Výpočet celkové ceny
        total_price = sum(item['price'] * item['quantity'] for item in cart_items)
        context['total_price'] = total_price

        return context









