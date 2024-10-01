from django.contrib import admin
from django.urls import path, include

from lzpplapp.views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users_app_url')),
]
