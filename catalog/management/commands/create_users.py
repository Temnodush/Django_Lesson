from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import CustomUser


class Command(BaseCommand):
    help = "Создаёт тестовых пользователей: обычный, модератор, админ"

    def handle(self, *args, **options):
        # Удаляем старых тестовых пользователей
        test_emails = ['user@test.com', 'moderator@test.com', 'admin@test.com']
        CustomUser.objects.filter(email__in=test_emails).delete()
        self.stdout.write("Старые тестовые пользователи удалены")

        # 1. Обычный пользователь
        user = CustomUser.objects.create_user(
            email='user@test.com',
            username='testuser',
            password='testpass123',
            first_name='Обычный',
            last_name='Пользователь',
            country='RU',
        )
        self.stdout.write(f"Создан пользователь: {user.email}")

        # 2. Модератор
        moderator = CustomUser.objects.create_user(
            email='moderator@test.com',
            username='moderator',
            password='testpass123',
            first_name='Модератор',
            last_name='Каталога',
            country='RU',
        )
        # Добавляем в группу модераторов
        moderator_group = Group.objects.get(name='Catalog Moderators')
        moderator.groups.add(moderator_group)
        self.stdout.write(f"Создан модератор: {moderator.email}")

        # 3. Админ
        admin = CustomUser.objects.create_superuser(
            email='admin@test.com',
            username='admin',
            password='testpass123',
            first_name='Админ',
            last_name='Системы',
            country='RU',
        )
        self.stdout.write(f"Создан админ: {admin.email}")

        self.stdout.write(self.style.SUCCESS("Все тестовые пользователи созданы!"))
        self.stdout.write("")
        self.stdout.write("Данные для входа:")
        self.stdout.write("  Пользователь: user@test.com / testpass123")
        self.stdout.write("  Модератор:    moderator@test.com / testpass123")
        self.stdout.write("  Админ:        admin@test.com / testpass123")
