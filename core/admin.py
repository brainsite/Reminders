from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Notification, RemindU


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = ('user_name', 'text_notification', 'datetime_notification', 'completed')


class RemindUAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'telegram')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'telegram', 'first_name', 'last_name', 'is_staff')


# Register your models here.
admin.site.register(RemindU, RemindUAdmin)
