from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Перезагружает тестовые данные для категорий и продуктов из фикстур"

    def handle(self, *args, **options):
        self.stdout.write("Удаляю старые данные...")

        # Сначала удаляем продукты, затем категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загружаю данные из фикстур...")

        # Загружаем фикстуру
        call_command("loaddata", "catalog/fixtures/catalog_data.json")

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены."))
