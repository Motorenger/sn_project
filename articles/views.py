from re import template
from unicodedata import category
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import *

class HomePage(ListView):
    model = SportsMen
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.all()
        context['categories'] = cat
        context['cat_count'] = cat.count()

        return context

class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.all()
        context['categories'] = cat
        context['cat_count'] = cat.count()

        context['sportsmens'] = SportsMen.objects.filter(category=kwargs['cat_id'])
        return context
    