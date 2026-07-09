from django.db import models
from parso.python.tree import Class

from users.models import CustomUser


# Create your models here.
# class StatusPublished(models.Model):
#     name = models.CharField(max_length=15, verbose_name="Статус публикации")
#     description = models.TextField(null=False, blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'статус публикации'
#         verbose_name_plural = 'статусы публикации'
#         ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=150 , verbose_name="Название категории")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

class Product(models.Model):
    STATUS_CHOICES = [
        ('OK','Опубликовано'),
        ('RE', 'Не прошло модерацию'),
        ('MD', 'Проходит модерацию'),
        ('NO', 'Не опубликовано'),
    ]

    name = models.CharField(max_length=150 , verbose_name="Наименование")
    description = models.TextField(null=True, blank=True , verbose_name="Описание")
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение', blank=True , null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    publish_status = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=True, null=True, default='NO')
    owner = models.ForeignKey(CustomUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ('can_unpublish', 'Can unpublish product'),
        ]

