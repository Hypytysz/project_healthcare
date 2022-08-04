from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def homepage(request):


    return render(
        request,
        "homepage.html",
        {'dane': "ALA MA KOTA"}
    )
