from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm
from django.views.generic import DeleteView, TemplateView, ListView, DetailView, UpdateView, CreateView
from django.core.mail import send_mail

from .models import Lead, Agent
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = 'leads/landing.html'


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'data'


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
    


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
