from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
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
        max_length=300,
        blank=True,
        verbose_name='Заметка о пользователе',
        help_text='Напишите заметку о себе'
    )

    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='Электронная почта пользователя',
        help_text='Введите свой электронный адрес'
    )

    confirmation_code = models.CharField(
        blank=True,
        verbose_name='Код для авторизации',
        max_length=16,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    @property
    def is_user(self):
        if self.role == 'user':
            return True
        else:
            return False

    @property
    def is_moderator(self):
        if self.role == 'moderator':
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.role == 'admin':
            return True
        else:
            return False
