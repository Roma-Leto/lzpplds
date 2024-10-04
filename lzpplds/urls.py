from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from lzpplapp.views import *

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('find/', find_users, name='find-users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
