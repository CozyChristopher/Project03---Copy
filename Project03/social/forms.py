from django import forms
from . import models


class UserInfoForm(forms.Form):
    birthday = forms.DateField(label='Birthday')
    employment = forms.CharField(label='Employment')
    location = forms.CharField(label='Location')
    interests = forms.CharField(label='Interests')
