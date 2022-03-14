from operator import mod
from re import M
from turtle import mode, title
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SportsMen(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    content = models.TextField()
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name