from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.


def home(request):
    name = 'Komal'
    return render(request, 'index.html', {'name': name})


def login(request):
    return render(request, 'firstapp\login.html')


def form_view(request):
    form = forms.Loginform
    return render(request, 'firstapp\\form.html', {'form': form})

def about(request):
    return HttpResponse("This is about page")


def contact(request):
    return HttpResponse("This is contact page")
