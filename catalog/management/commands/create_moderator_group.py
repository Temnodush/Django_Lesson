from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Создаёт группу модераторов в каталоге товаров."

    def handle(self, *args, **options):
        group_name = "Catalog Moderators"

        # Удаляем группу, если она уже существует.
        Group.objects.filter(name=group_name).delete()

        # Создаём новую.
        catalog_moderators = Group.objects.create(name=group_name)
        self.stdout.write(f"Группа {group_name} создана заново")

        # Назначаем права.
        delete_product = Permission.objects.get(codename="delete_product")
        can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
        catalog_moderators.permissions.add(delete_product, can_unpublish_product)

        self.stdout.write(self.style.SUCCESS("Права успешно добавлены"))