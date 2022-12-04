from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from jinja2 import Environment, FileSystemLoader
import pdfkit

from .models import *
from .forms import *
from .utils import *


def main_page(request):
    context = {'menu': menu, 'title': 'Main page'}
    return render(request, 'resume/index.html', context=context)


def about(request):
    return render(request, 'resume/about.html', {'menu': menu, 'title': 'О сайте'})


def new_form(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('after_form')
    else:
        form = AddForm()
    return render(request, 'resume/newform.html', {'form': form})


def after_form(request):
    form = CVInfo.objects.first().pk
    info = CVInfo.objects.get(pk=form)
    print(info)
    context = {'info': info, 'menu': menu}
    return render(request, 'resume/cv_template.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'resume/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'resume/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


def get_pdf(request):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("pdf_template.html")
    pdf_template = template.render({'menu': menu})

