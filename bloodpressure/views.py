from .models import Bloodpressure
from .forms import BloodpressureForm
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def homepage(request):
    form = BloodpressureForm(request.POST)
    return render(request, "homepage.html", {"homepage": form})


def listaPomiarow(request):
    pomiary = Bloodpressure.objects.all()
    return render(request, "listaPomiarow.html", {"listaPomiarow": pomiary})


def dodajPomiar(request):
    if request.method == "POST":
        form = BloodpressureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage.html")
    else:
        form = BloodpressureForm()
    return render(request, "dodajPomiar.html", {"formularz": form})


def edytujPomiar(request, pk):
    pomiar = get_object_or_404(Bloodpressure, pk=pk)
    if request.method == "POST":
        form = BloodpressureForm(request.POST, instance=pomiar)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = BloodpressureForm(instance=pomiar)

    return render(request, "edytujPomiar.html", {"formularz": form})


def usunPomiar(request, pk):
    Bloodpressure.objects.filter(pk=pk).delete()
    return redirect("homepage")


# def pomiary_poranne_systolic(request):
#     pomiary = Bloodpressure.objects.filter(systolic=100)
#     return render(request, "listaPomiarow.html", {"listaPomiarow": pomiary})
