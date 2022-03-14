from django.urls import path, include

from .views import *

urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('category/<str:category>', CategoryView.as_view(), name='category'),
]