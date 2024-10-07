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
    agents = Agent.objects.all()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            description = form.cleaned_data['description']
            agent = form.cleaned_data['agent']

            my_object = Lead(first_name=first_name,
                             last_name=last_name,
                             age=age,
                             description=description,
                             agent=agent)

            my_object.save()
            return redirect('/leads')
    else:
        form = LeadModelForm()

    context = {
        "form": form,
        "agents": agents
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