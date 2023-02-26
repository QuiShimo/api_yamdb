from rest_framework import serializers

from reviews.models import Category, Comments, Genre, Review, Title
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class AuthTokenserializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        required=True,
        max_length=16,
    )


class GanreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        lookup_field = 'slug'
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


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

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user

        if Review.objects.filter(
            author=author, title=title_id
        ).exists():
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
        models = Comments
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('pub_date',)
