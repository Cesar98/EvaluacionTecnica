from django.http import HttpResponse;
from django.template import Template, Context, loader;
from django.shortcuts import render;

def home(request):
    return render(request, 'home.html')

def list_employees(request):
    return render(request, 'listEmployees.html')