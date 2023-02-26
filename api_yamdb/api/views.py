from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.models import User
from users.token import get_tokens_for_user

from .serializers import AuthTokenserializer, SignUpSerializer
from .utils import generate_and_send_confirmation_code_to_email


@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    if not User.objects.filter(username=username).exists():
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['username'] != 'me':
            serializer.save()
            generate_and_send_confirmation_code_to_email(username)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            'Username указан неверно!', status=status.HTTP_400_BAD_REQUEST
        )
    user = get_object_or_404(User, username=username)
    serializer = SignUpSerializer(
        user, data=request.data, partial=True
    )
    serializer.is_valid(raise_exception=True)
    if serializer.validated_data['email'] == user.email:
        serializer.save()
        generate_and_send_confirmation_code_to_email(username)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(
        'Почта указана неверно!', status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def get_token(request):
    serializer = AuthTokenserializer(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(User, username=request.data['username'])
        confirmation_code = serializer.data.get('confirmation_code')
        if confirmation_code == str(user.confirmation_code):
            return Response(get_tokens_for_user(user),
                            status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
