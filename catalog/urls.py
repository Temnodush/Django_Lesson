from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('', views.home, name='home'),          # главная страница
    # path('contacts/', views.contacts, name='contacts'),  # страница контактов
    # path('products/<int:pk>/', views.product_detail, name='product_detail'), # страница продукта
    # path('product_list/', views.product_list, name='product_list'), # список продуктов
]