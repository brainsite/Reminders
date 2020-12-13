from datetime import datetime

from django.core.mail import send_mail

from Reminders.celery import app
from .models import Notification
from .utils import send


@app.task
def send_notification():
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M')
    for contact in Notification.objects.filter(datetime_notification__lte=date_now).filter(completed=False):
        send_mail(
            subject='Тестовые письма',
            message=contact.text_notification + ' ' + str(contact.datetime_notification),
            from_email='rent@brainsite.ru',
            recipient_list=[contact.user_name.email],
            fail_silently=False,
        )
        contact.completed = True
        contact.save()
