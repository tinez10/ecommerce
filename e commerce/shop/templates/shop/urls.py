# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
]
