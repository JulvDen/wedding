from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def home_view_fr(request, *args, **kwargs):
    return render(request, "fr/index.html", {})

