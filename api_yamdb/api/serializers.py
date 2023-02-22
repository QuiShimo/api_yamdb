from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from users.models import User


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserSignUp(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        required=True,
        max_length=16,
    )


