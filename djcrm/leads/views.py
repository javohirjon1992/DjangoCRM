from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead": lead,
    }
    return render(request, "leads/lead_detail.html", context)



def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)

    context = {
        "form": LeadForm()
    }
    return render(request, "leads/lead_create.html", context)
