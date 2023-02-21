from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название',
                            help_text='Необходимо названия котегории')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Индификатор',
                            help_text='Необходим индификатор категории')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название',
                            help_text='Необходимо названия жанра')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Идентификатор',
                            help_text='Необходим индификатор жанра')

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название',
                            help_text='Необходимо названия произведения')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание',
                                   help_text='Необходимо описание')
    year = models.IntegerField(verbose_name='Дата выхода',
                               help_text='Укажите дату выхода')
    category = models.ForeignKey(Category,
                                 related_name='titles',
                                 verbose_name='Катигория',
                                 help_text='Укажите категорию')
    genres = models.ManyToManyField(Category,
                                    related_name='titles',
                                    verbose_name='Жанр',
                                    help_text='Укажите жанр')

    def __str__(self):
        return self.name
