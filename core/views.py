
from django.http import request
from django.shortcuts import render,redirect

# Create your views here.

def Home(request):
    return render(request, 'inicio.html')

def Platos(request):
    return render(request, 'platos.html')

def Mobile(request):
    return render(request, 'mobile.html')

