from django.urls import path

from .views import *

urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('category/<int:cat_id>', CategoryView.as_view(), name='category'),
]