from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm

from .models import Lead, Agent

def landing_page(request):
    return render(request, 'leads/landing.html')

def lead_detail(request, pk):
    context = {
        'data': Lead.objects.get(pk=pk)
    }
    return render(request, 'leads/lead_detail.html', context=context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)

    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return redirect('/leads')


    context = {
        "lead": lead,
        'form': form
    }

    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):
    obj = Lead.objects.get(pk=pk)
    obj.delete()
    return redirect('leads:lead_list')

def lead_list(request):
    context = {
        'leads': Lead.objects.all()
    }

    return render(request, 'leads/lead_list.html', context)