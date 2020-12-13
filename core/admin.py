from django.contrib import admin

from .models import Notification, RemindU


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = ('user_name', 'text_notification', 'datetime_notification', 'completed')

@admin.register(RemindU)
class RemindUAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'lang')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'telegram','lang', 'first_name', 'last_name', 'is_staff')

# Register your models here.
