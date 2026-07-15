from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('moderation/', views.ModerationListView.as_view(), name='moderation_list'),
    path('moderation/<int:pk>/', views.ModerateProductView.as_view(), name='moderate_product'),
    path('category/<int:category_id>/', views.CategoryProductsView.as_view(), name='category_products'),
]
