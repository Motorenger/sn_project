from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import *

class HomePage(ListView):
    model = SportsMen
    template_name = 'home.html'

class CategoryView(TemplateView):
    template_name = 'category.html'
    