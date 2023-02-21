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
        verbose_name='Уровень доступа пользователя',
        help_text='Уровень доступа пользователя'
    )

    bio = models.TextField(
        'Биография',
        max_length=300,
        blank=True,
        verbose_name='Заметка о пользователе',
        help_text='Напишите заметку о себе'
    )

    email = models.EmailField(
        'Адрес электронной почты',
        blank=False,
        unique=True,
        verbose_name='Электронная почта пользователя',
        help_text='Введите свой электронный адрес'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'