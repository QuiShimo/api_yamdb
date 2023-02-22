import random

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegister, UserSignUp
from users.models import User

from users.mailing import mail_code

from users.token import get_tokens_for_user


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegister(data=request.data)
    if serializer.is_valid() and request.data['username'] != 'me':
        confirmation_code = int(''.join([str(random.randrange(0, 10))
                                         for _ in range(16)]))
        email = request.data['email']
        username = request.data['username']
        user = User.objects.filter(username=username).exists()
        if not user:
            User.objects.create(email=email, username=username,
                                confirmation_code=confirmation_code)
        else:
            User.objects.filter(username=username).update(
                confirmation_code=confirmation_code
            )
        mail_code(email, username, confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_token(request):
    serializer = UserSignUp(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(User, username=request.data['username'])
        confirmation_code = serializer.data.get('confirmation_code')
        if confirmation_code == str(user.confirmation_code):
            return Response(get_tokens_for_user(user),
                            status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
