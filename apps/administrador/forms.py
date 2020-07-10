from django import forms
from django.forms import ModelForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import Habitacion

class CustomUserForm(UserCreationForm):
    pass

