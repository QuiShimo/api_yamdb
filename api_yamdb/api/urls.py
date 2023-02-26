from django.urls import include, path
from rest_framework.routers import DefaultRouter


from api.views import (CategoryViewSet, CommentsViewSet, ReviewViewSet,
                       get_token, signup)


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/signup/', signup, name='user-registration'),
    path('v1/auth/token/', get_token, name='user_get_token'),
    path('v1/', include(router.urls)),
]
