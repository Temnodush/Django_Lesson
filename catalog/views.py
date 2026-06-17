from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()[:3]

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'



# def home(request):
#     """Контроллер для главной страницы"""
#     products = Product.objects.all()[:3]
#     context = {'products': products}
#     return render(request, 'catalog/home.html', context)
#
# def contacts(request):
#     """Контроллер для страницы контактов"""
#     return render(request, 'catalog/contacts.html')
#
# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/product_list.html', context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context)