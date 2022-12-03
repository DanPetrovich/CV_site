from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class AddForm(forms.Form):
    name = forms.CharField(max_length=15, label="name")
    lastname = forms.CharField(max_length=20, label="lastname")
    birth_date = forms.DateField(label="birth_date")
    # photo = forms.ImageField()
    phone_number = forms.SlugField(label="phone_number")
    email = forms.EmailField(max_length=40, label="email")
    skills = forms.SlugField(label="skills")

    def clean_phone(self):
        phone = self.clean_data('phone_number')
        if len(phone) != 11:
            raise ValidationError("Некорректный номер телефона")
        return phone


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

