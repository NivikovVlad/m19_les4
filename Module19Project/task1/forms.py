from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин', required=True)
    password = forms.CharField(min_length=8, max_length=30, widget=forms.PasswordInput(),
                               label='Введите пароль', required=True)
    repeat_password = forms.CharField(min_length=8, max_length=30, widget=forms.PasswordInput(),
                                      label='Повторите пароль', required=True)
    age = forms.IntegerField(max_value=100, label='Введите свой возраст', required=True)