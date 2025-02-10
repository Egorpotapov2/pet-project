# from django import forms
#
# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=100, label="Логин")
#     password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#
#         if password != confirm_password:
#             raise forms.ValidationError("Пароли не совпадают!")
