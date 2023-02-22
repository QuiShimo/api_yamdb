from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import user_registration, get_token

router_v1 = DefaultRouter()

urlpatterns = [
    path('v1/auth/signup/', user_registration, name='user-registration'),
    path('v1/auth/token/', get_token, name='user_get_token'),
]
