from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User


class HomePage(TemplateView):
    template_name = 'lzpplapp/index.html'
