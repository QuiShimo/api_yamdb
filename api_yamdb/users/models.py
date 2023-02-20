from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Модель пользователя'''
    CHOICES = (
        ('user', 'Аутентифицированный пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Админ'),
    )
    role = models.CharField(
        max_length=16,
        choices=CHOICES,
        default='user',
    )

    bio = models.TextField(
        'Биография',
        max_length=300,
        blank=True,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        blank=False,
        unique=True,

    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
