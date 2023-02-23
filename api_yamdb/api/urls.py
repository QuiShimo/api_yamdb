from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, ReviewViewSet, GenreViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genre', GenreViewSet, basename='genre')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
