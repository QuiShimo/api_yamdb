from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from ..users.mailing import mail_code
#from ..users.models import User
from .serializers import UserRegister


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegister(data=request.data)
    if serializer.is_valid():
        email = request.data['email']
        username = request.data['username']
        #confirmation_code = generate code
        #save_code_to_model
        #mail_code(email, username, confirmation_code)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
