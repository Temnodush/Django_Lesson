from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import  get_object_or_404
from django.urls import reverse_lazy
from django.conf import settings
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, ModerateProductForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from catalog.services import get_products_by_category
from catalog.models import Category
import logging

logger = logging.getLogger(__name__)
CACHE_TTL = getattr(settings, "CACHE_TTL", 60 * 15)


class ModerationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/moderation_list.html'
    context_object_name = 'products'
    permission_required = 'catalog.can_unpublish_product'

    def get_queryset(self):
        return super().get_queryset().filter(publish_status='MD')


class ModerateProductView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ModerateProductForm
    template_name = 'catalog/moderation_form.html'
    context_object_name = 'product'
    permission_required = 'catalog.can_unpublish_product'
    success_url = reverse_lazy('catalog:moderation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            cache.delete("product_list")
            cache.delete(f"category_{self.object.category_id}")
            cache.delete(f"product_{self.object.pk}")
        except Exception:
            logger.exception("Ошибка при инвалидировании кэша в ModerateProductView")
        return response


class ProductCreateView(LoginRequiredMixin ,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.publish_status = 'MD'
        response = super().form_valid(form)

        try:
            cache.delete("product_list")
            cache.delete(f"category_{form.instance.category_id}")
        except Exception:
            logger.exception("Ошибка при инвалидировании кэша в ProductCreateView")
        return response

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.can_unpublish_product')

    def form_valid(self, form):
        product = self.get_object()
        old_category_id = product.category_id
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        try:
            cache.delete("product_list")
            cache.delete(f"category_{form.instance.category_id}")
            if old_category_id and old_category_id != form.instance.category_id:
                cache.delete(f"category_{old_category_id}")
        except Exception:
            logger.exception("Ошибка при инвалидировании кэша в ProductUpdateView")
        return response

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.delete_product')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        category_id = obj.category_id
        pk = obj.pk
        response = super().delete(request, *args, **kwargs)
        try:
            cache.delete("product_list")
            if category_id:
                cache.delete(f"category_{category_id}")
            cache.delete(f"product_{pk}")
        except Exception:
            logger.exception("Ошибка при инвалидировании кэша в ProductDeleteView")
        return response


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publish_status='OK')[:3]

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = cache.get("product_list")

        if queryset:
            return queryset
        else:
            queryset = super().get_queryset().filter(publish_status='OK')
            result = list(queryset)
            cache.set("product_list", result, settings.CACHE_TTL)
            return result


@method_decorator(cache_page(settings.CACHE_TTL), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'



class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = get_object_or_404(Category, pk=category_id)
        return context
