from rest_framework import serializers
from reviews.models import Title, Genre, Category


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
