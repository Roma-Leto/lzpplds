from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm, PasswordChangeForm

from .models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'email',
            'date_of_birth',
            'sex',
        )
        labels = {
            'email': 'E-mail',
            'first_name': "Имя",
            'last_name': "Фамилия",
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )


class EditProfileUserForm(forms.ModelForm):
    """ Класс формы для ввода изменяемых данных пользователя """
    # поля ниже обязательны для заполнения
    about_me = forms.CharField(
        label="О себе",
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите немного о себе',
            'class': 'form-control',
            'help': 'Увлечения или интересы',
        }
        )
    )
    sex = forms.ChoiceField(
        label="Пол",
        widget=forms.Select, choices=User.SEX_CHOICES
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'photo',
            'last_name',
            'email',
            'about_me',
            'date_of_birth',
            'sex',
            'city',
        )
