from django.shortcuts import render, redirect
from .models import RegistrationForm
from .models import User
from django.contrib.auth import authenticate, login

from django.contrib import messages


def logi(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            # return redirect('./success.html')  # Перенаправление на главную страницу после успешного входа
            return render(request, 'vh')
        else:
            error = "Неверный логин или пароль"
    return render(request, 'reg/vhod.html', {'error': error})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()  # Сохраняем пользователя
            return redirect('success')  # Перенаправляем на страницу успеха
    else:
        form = RegistrationForm()
    return render(request, 'reg/regist.html', {'form': form})


def success (request):
    return render(request, "reg/success.html")


