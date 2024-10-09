from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm
from django.views.generic import DeleteView, TemplateView, ListView, DetailView, UpdateView, CreateView
from django.core.mail import send_mail

from .models import Lead, Agent

class LandingPageView(TemplateView):
    template_name = 'leads/landing.html'


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'data'


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message='Go to the site to see ur new lead',
            from_email="test@test.com"
            recipient_list=['te ']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
