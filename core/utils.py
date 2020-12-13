from django.core.mail import send_mail


def send(email, message):
    send_mail(
        subject='Тестовые письма',
        message=message,
        from_email='rent@brainsite.ru',
        recipient_list=[email],
        fail_silently=False,
    )
