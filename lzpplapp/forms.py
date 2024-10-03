from random import choices

from django import forms
from users.models import User


class FindUsers(forms.Form):
    lte = forms.IntegerField(label='Младше', min_value=18, initial=100)
    gte = forms.IntegerField(label='Старше', initial=18)
    sex = forms.ChoiceField(choices=User.SEX_CHOICES, label='Пол')
