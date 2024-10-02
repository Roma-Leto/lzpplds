from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, \
    DetailView

from users.forms import UserLoginForm, RegisterUserForm
from users.models import User


class UserLogin(LoginView):
    form_class = UserLoginForm  # default: AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация',
    }

    # Переопределение функции перенаправления после успешной авторизации.
    # По умолчанию - profile
    def get_success_url(self):
        return reverse_lazy("index")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = 'users/register.html'
    extra_context = {
        'title': "Регистрация",
    }
    success_url = reverse_lazy('users:login-done')


class LoginDoneView(TemplateView):
    template_name = 'users/login_done.html'


class ProfileUserView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'


class EditProfileUserView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    pass
