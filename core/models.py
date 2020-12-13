from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class RemindU(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField('Email address', unique=True)
    username = models.CharField('username', max_length=150, unique=True)
    REQUIRED_FIELDS = ['username']  # removes email from REQUIRED_FIELDS
    telegram = models.CharField('Telegram', max_length=20, blank=True, null=False)


class Notification(models.Model):
    """ Уведомления/напоминания """
    user_name = models.ForeignKey(RemindU, on_delete=models.CASCADE)
    text_notification = models.TextField(verbose_name="Текст напоминания", blank=True, null=True)
    datetime_notification = models.DateTimeField('DateTime Notification', blank=True, null=True)
    completed = models.BooleanField('Completed', default=False)

    def __str__(self):
        return self.user_name.email
