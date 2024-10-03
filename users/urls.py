from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('login-done/', LoginDoneView.as_view(), name='login-done'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/edit/', EditProfileUserView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', profile_user, name='profile'),
]
