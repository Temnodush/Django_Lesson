from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    COUNTRY_CHOICES = [
        ('RU', 'Россия'),
        ('KZ', 'Казахстан'),
        ('CN', 'Китай'),
        ('MN', 'Монголия'),
        ('UA', 'Украина'),
        ('BY', 'Беларусь'),
        ('FI', 'Финляндия'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, blank=True, null=True, default='RU')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email