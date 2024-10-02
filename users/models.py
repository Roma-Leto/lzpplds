from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/photos/%Y/%m/%d",
        blank=True,
        null=True,
        verbose_name="Фотография",
        default='users/photos/default_user.jpg')
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    about_me = models.CharField(max_length=1000,
                                blank=True,
                                verbose_name="О себе")
    city = models.CharField(max_length=100)

    SEX_CHOICES = [
        ('male', 'Парень'),
        ('female', 'Девушка'),
    ]

    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    REQUIRED_FIELDS = ["date_of_birth"]  # для запроса при регистрации
    # суперпользователя
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ['-date_joined', 'first_name', ]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
