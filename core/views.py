from datetime import datetime

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NotificationForm, RegisterForm
from .models import Notification


@login_required(login_url='/login')
def create_schedule(request):
    if 'save' in request.POST:
        form = NotificationForm(request.POST)
        filtred_not = []
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = NotificationForm()
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M')
        filtred_not = Notification.objects.filter(datetime_notification__lte=date_now)
    return render(request, 'notis.html', {'form': form, 'notifi': filtred_not})


def thanks(request):
    return render(request, 'thanks.html')


#### Register and LogIn

def registry(request):
    if 'register' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    return render(request, 'registry.html')

def login(request):
    if 'login' in request.POST:
        # c.update(csrf(request))
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/")
        else:
            # Отображение страницы с ошибкой
            return HttpResponseRedirect("/account/invalid/")
    return render(request, 'signin.html')
