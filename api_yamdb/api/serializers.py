import datetime as dt
from rest_framework import serializers

from api.permissions import IsAdminOrStaff
from reviews.models import Category, Comments, Genre, Review, Title
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        required=True,
        max_length=16,
    )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='slug')
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug')

    rating = serializers.IntegerField(read_only=True)


    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        year = dt.date.today().year
        if not (value <= year):
            raise serializers.ValidationError('Некоректный год.')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'pub_date')
        read_only_fields = ('pub_date', )

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка должна быть от 1 до 10')
        return value

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user

        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                ('Ошибка добавления отзыва к произведению: '
                 'вы уже добавляли отзыв к этопу произведению.')
            )
        return data


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('pub_date',)


class UserSerializer(serializers.ModelSerializer):
    permission_classes = [IsAdminOrStaff]

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )
