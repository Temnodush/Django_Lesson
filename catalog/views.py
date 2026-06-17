from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    """Контроллер для главной страницы"""
    products = Product.objects.all()[:3]
    context = {'products': products}
    return render(request, 'home.html', context)

def contacts(request):
    """Контроллер для страницы контактов"""
    return render(request, 'contacts.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)