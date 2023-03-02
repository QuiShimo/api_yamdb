import random

from django.conf import settings
from django.core.mail import send_mail
from rest_framework.generics import get_object_or_404

from users.models import User


def send_confirmation_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = int(
        ''.join([str(random.randrange(0, 10))
                 for _ in range(settings.CONFIRMATION_CODE_LENGTH)])
    )
    user.confirmation_code = confirmation_code
    send_mail(
        'Код подтвержения для завершения регистрации',
        f'Ваш код для получения JWT токена {user.confirmation_code}',
        settings.ADMIN_EMAIL,
        (user.email,),
        fail_silently=False,
    )
    user.save()
