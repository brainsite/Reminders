from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notification, RemindU


class NotificationForm(forms.ModelForm):
    """ Форма для создания напоминаний """

    class Meta:
        model = Notification
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False, help_text='По желанию')
    last_name = forms.CharField(max_length=30, required=False, help_text='По желанию')
    username = forms.CharField(max_length=30, required=True, help_text='По желанию')

    class Meta:
        model = RemindU
        fields = ["email", "password1", "password2", 'first_name', 'last_name', 'username']