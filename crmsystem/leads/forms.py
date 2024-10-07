from django import forms
from .models import Lead, Agent

class LeadModelForm(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    agent = forms.ModelChoiceField(queryset=Agent.objects.all())