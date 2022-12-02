from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .models import *
from .forms import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Создать резюме", 'url_name': 'form'},
        {'title': "Войти", 'url_name': 'login'}]


def main_page(request):
    context = {'menu': menu, 'title': 'Main page'}
    return render(request, 'resume/index.html', context=context)


def about(request):
    return render(request, 'resume/about.html', {'menu': menu, 'title': 'О сайте'})


def new_form(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            CVInfo.objects.create(**form.cleaned_data)
            return redirect('after_form')
    else:
        form = AddForm()
    return render(request, 'resume/newform.html', {'form': form})


def after_form(request):
    return render(request, 'resume/after_form.html',
                  {{'menu': menu, 'title': 'Поздравляем, Вы успешно зарегистрировались'}})


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'resume/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'resume/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
