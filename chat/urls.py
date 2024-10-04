from django.urls import path
from chat import views as chat
from . import views

app_name = 'chat'

urlpatterns = [
    path("", chat.chat_view, name="chat_page"),
    path('<int:recipient_id>/', views.chat_view, name='chat'),
]