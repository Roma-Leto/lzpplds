from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, \
    DetailView

from lzpplapp.forms import FindUsers
from users.forms import UserLoginForm, RegisterUserForm, EditProfileUserForm
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


@login_required  # Будет доступно только авторизованным пользователям
def profile_user(request, username: str):
    try:
        user = User.objects.filter(username=username)
    except User.DoesNotExist:
        return HttpResponseNotFound('Пользователь не найден')
    context = {
        'users': user,
        'title': 'Профиль'
    }
    return render(request, "users/user_detail.html", context)


@login_required  # Будет доступно только авторизованным пользователям
def profile_find_user(request, username: str):
    try:
        users = User.objects.filter(username=username)
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseNotFound('Пользователь не найден')
    context = {
        'users': users,
        'user': user,
        'title': 'Профиль'
    }
    return render(request, "users/user_find_detail.html", context)


class EditProfileUserView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile_edit.html'
    form_class = EditProfileUserForm
    success_message = 'Данные профиля пользователя изменены.'

    # def setup(self, request, *args, **kwargs):
    #     """
    #     Функция извлечения из модели текущего пользователя
    #     ключа пользователя.
    #     """
    #     self.user_id = request.user.pk
    #     self.username = request.user.username
    #     return super().setup(request, *args, **kwargs)

    # def get_object(self, queryset=None):
    #     """
    #     Функция извлечения исправляемой записи.
    #     """
    #     if not queryset:
    #         queryset = self.get_queryset()
    #     return get_object_or_404(queryset, pk=self.user_id,
    #                              username=self.username)
    #
    # def get_success_url(self):
    #     return reverse('users:profile', args=[self.username])

# class EditProfileUserView(SuccessMessageMixin, LoginRequiredMixin,
#                           UpdateView):
#     model = User
#     template_name = 'users/profile_edit.html'
#     form_class = EditProfileUserForm
#     success_message = 'Данные профиля пользователя изменены.'
#
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user = request.user

    def get_object(self, queryset=None):
        return self.user

    def get_success_url(self):
        return reverse('users:profile', args=[self.user.username])
