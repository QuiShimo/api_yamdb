from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import user_registration

router_v1 = DefaultRouter()

urlpatterns = [
    path('v1/auth/signup/', user_registration, name='user-registration'),
]
