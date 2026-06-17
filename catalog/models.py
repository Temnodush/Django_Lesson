from django.db import models

# Create your models here.

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
    name = models.CharField(max_length=150 , verbose_name="Наименование")
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(help_text="Цена товара")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

