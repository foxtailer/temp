from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from main.models import User


class UserLoginForm(AuthenticationForm):
  username = forms.CharField() 
  password = forms.CharField()

  class Meta:
    model = User


class UserRegistrationForm(UserCreationForm):

  class Meta:
    model = User
    fields = (
      "username",
      "password1",
      "password2",
    )
  
  username = forms.CharField()
  password1 = forms.CharField()
  password2 = forms.CharField()