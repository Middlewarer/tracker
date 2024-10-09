from django.forms import ModelForm
from .models import Lead, Agent
from django import forms

class LeadModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'description', 'agent')