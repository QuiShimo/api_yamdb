from django.core.mail import send_mail


def mail_code(email, username, confirmation_code):
    send_mail(
        f'{username}, Ваш код для регистрации',
        f'Your confirmation_code: {confirmation_code}',
        'register@yamdb.com',  # Это поле "От кого"
        [f'{email}'],  # Это поле "Кому" (можно указать список адресов)
        fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
    )
