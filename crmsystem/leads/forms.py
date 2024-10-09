from django.forms import ModelForm
from .models import Lead, Agent
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User=get_user_model()

class LeadModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'description', 'agent')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}