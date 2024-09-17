from django.shortcuts import render
from django.views.generic import TemplateView

from viewer.models import Categorie

class MainPageView(TemplateView):
    template_name = 'main.html'
    extra_context = {
    "all_categories": Categorie.objects.all()

    }




