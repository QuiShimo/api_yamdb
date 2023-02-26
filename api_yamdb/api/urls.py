from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import get_token, signup

router_v1 = DefaultRouter()

urlpatterns = [
    path('v1/auth/signup/', signup, name='user-registration'),
    path('v1/auth/token/', get_token, name='user_get_token'),
]
