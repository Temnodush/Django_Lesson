from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),          # главная страница
    path('contacts/', views.contacts, name='contacts'),  # страница контактов
    path('products/<int:pk>/', views.product_detail, name='product_detail'), # страница продукта
    path('product_list/', views.product_list, name='product_list'), # список продуктов
]