from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = ('user_name', 'text_notification', 'datetime_notification', 'completed')

# Register your models here.
