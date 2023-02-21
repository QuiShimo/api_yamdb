from rest_framework import serializers
from reviews.models import Review


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
