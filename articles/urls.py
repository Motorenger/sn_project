from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('category/<int:cat_id>', CategoryView.as_view(), name='category'),
	path('detail/<int:pk>', DetailView.as_view(), name='detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)