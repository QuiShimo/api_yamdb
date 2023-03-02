from csv import DictReader

from django.core.management.base import BaseCommand

from api_yamdb.settings import BASE_DIR
from reviews.models import Category, Comments, Genre, GenreTitle, Review, Title
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Импорт данных из csv файлов'

    def ImportUser(self):
        if CustomUser.objects.exists():
            print('Данные для User уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/users.csv',
                    encoding='utf8')):
                CustomUser.objects.create(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],)
            print('Данные для User загружены')

    def ImportGenre(self):
        if Genre.objects.exists():
            print('Данные для Genre уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/genre.csv',
                    encoding='utf8')):
                Genre.objects.create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],)
            print('Данные для genre загружены')

    def ImportCategory(self):
        if Category.objects.exists():
            print('Данные для Category уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/category.csv',
                    encoding='utf8')):
                Category.objects.create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],)
            print('Данные для Category загружены')

    def ImportTitle(self):
        if Title.objects.exists():
            print('Данные для Title уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/titles.csv',
                    encoding='utf8')):
                Title.objects.create(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Category.objects.get(id=row['category']),)
            print('Данные для Title загружены')

    def ImportGenreTitle(self):
        if GenreTitle.objects.exists():
            print('Данные для GenreTitle уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/genre_title.csv',
                    encoding='utf8')):
                GenreTitle.objects.create(
                    id=row['id'],
                    title_id=row['title_id'],
                    genre_id=row['genre_id'],)
            print('Данные для GenreTitle загружены')

    def ImportReview(self):
        if Review.objects.exists():
            print('Данные для Review уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/review.csv',
                    encoding='utf8')):
                Review.objects.create(
                    id=row['id'],
                    title_id=row['title_id'],
                    text=row['text'],
                    author=CustomUser.objects.get(id=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date'],)
            print('Данные для Review загружены')

    def ImportComments(self):
        if Comments.objects.exists():
            print('Данные для Comments уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / 'static/data/comments.csv',
                    encoding='utf8')):
                Comments.objects.create(
                    id=row['id'],
                    review_id=row['review_id'],
                    text=row['text'],
                    author=CustomUser.objects.get(id=row['author']),
                    pub_date=row['pub_date'],)
            print('Данные для Comments загружены')

    def handle(self, *args, **kwargs):
        self.ImportUser()
        self.ImportGenre()
        self.ImportCategory()
        self.ImportTitle()
        self.ImportGenreTitle()
        self.ImportReview()
        self.ImportComments()
