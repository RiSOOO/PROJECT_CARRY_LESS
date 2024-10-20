from django.contrib.auth.forms import (UserCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from viewer.forms import ProductsForm
from viewer.models import CartItem
from viewer.models import Categorie
from viewer.models import Invoice
from viewer.models import Product


class MainPageView(TemplateView):
    template_name = 'main.html'
    extra_context = {

        "all_categories": Categorie.objects.all(),
        "all_products": Product.objects.all()

    }


class CategoriesView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        category_id = request.GET.get("id")


        if(category_id == None):
            extra_context = {
                "all_categories": Categorie.objects.all()
            }
        else:
            extra_context={
                "all_categories": Categorie.objects.all(),
                "category": Categorie.objects.get(id=category_id),
                "products": Product.objects.filter(products_of_categories=category_id)
            }
        return render(request,"kategorie.html",extra_context)


class ProductsView(PermissionRequiredMixin, TemplateView):
    template_name = "produkty.html"
    extra_context = {
    "all_products": Product.objects.all()
    }
    permission_required = "viewer.view_product"


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


class ViewCart(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(user=self.request.user)
        context['cart_items'] = cart_items

        # Výpočet celkové ceny
        total_price = sum(item.total_price() for item in cart_items)
        context['total_price'] = total_price

        return context


class AddToCartView(View):
    def post(self, request, *args, **kwargs):

        user = request.user

        # Získání produktu na základě předaného ID (pk)
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_id)

        # Získání nebo vytvoření položky v košíku
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=user,
            defaults={'quantity': 1}
        )

        # Pokud už existuje, zvýšíme množství
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Přesměrování na stránku košíku po přidání produktu
        return redirect('ViewCart')  # Tento název URL musí odpovídat cestě k ViewCart


class RemoveFromCartView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        user = request.user
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_id)
        cart_item = CartItem.objects.get(
            product=product,
            user=user
        )
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('ViewCart')


class CheckoutView(View):
    def get(self, request):
        # Vykreslení stránky checkout, pokud je požadavek typu GET
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price for item in cart_items)
        cart_items.delete()

        # Výpočet celkové ceny
        return render(request, 'checkout.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })




class InvoiceView(LoginRequiredMixin, View):
    template_name = 'invoice.html'  # Cesta k vaší šabloně pro checkout

    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        return render(request, self.template_name, context={
            "name": Invoice.objects.filter(user=logged_in_user)
        })














