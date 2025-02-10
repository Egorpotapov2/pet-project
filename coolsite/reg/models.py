from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # Для хэширования пароля

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует.')
        return username,

    def save(self):
        # Получаем данные из формы
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        # Хэшируем пароль
        # hashed_password = make_password(password)

        user = User.objects.create_user(
            username=username,
            password=password
        )
        # Создаем и сохраняем пользователя
        # user = User(username=username, password=hashed_password)
        user.save()
