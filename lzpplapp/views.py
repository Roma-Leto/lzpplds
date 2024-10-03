from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from lzpplapp.forms import FindUsers
from users.models import User


class HomePage(TemplateView):
    template_name = 'lzpplapp/index.html'


@login_required
def find_users(request):
    today = datetime.now().date()
    if request.method == 'POST':
        form = FindUsers(request.POST)
        if form.is_valid():
            find_age_l = form.cleaned_data["lte"]
            find_age_h = form.cleaned_data["gte"]
            sex = form.cleaned_data["sex"]
            filt_l = today.year - find_age_l
            filt_h = today.year - find_age_h
            users = User.objects.filter(
                Q(date_of_birth__gte=f'{filt_l}-01-01')
                & Q(date_of_birth__lte=f'{filt_h}-01-01')
                & Q(sex=sex)
            )
            old = [today.year - user.date_of_birth.year for user in users]
            old.reverse()
            content = {
                'today': today,
                'users': users,
                'old': old,
                'form': form,
            }
    else:
        form = FindUsers()
        content = {
            'form': form,
        }
    return render(request, 'lzpplapp/find-form-page.html', content)
