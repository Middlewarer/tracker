from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm

from .models import Lead, Agent

class LeadListView(View):

    template_name = "leads/lead_list.html"
    
    def get(self, request):
        leads = Lead.objects.all()
        context = {
            'leads': leads
        }

        return render(request, self.template_name, context)

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

