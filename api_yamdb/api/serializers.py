from rest_framework import serializers

from users.models import User


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
