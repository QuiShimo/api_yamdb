from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.serializers import (CategorySerializer, CommentsSerializer,
                             ReviewSerializer)
from reviews.models import Category, Review, Title


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=int(self.kwargs.get('title_id')))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=int(self.kwargs.get('title_id')))
        return title.reviews.all()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=int(self.kwargs.get('review_id')),
            title__id=int(self.kwargs.get('title_id'))
        )
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=int(self.kwargs.get('review_id')),
            title__id=int(self.kwargs.get('title_id'))
        )
        return review.comments.all()
