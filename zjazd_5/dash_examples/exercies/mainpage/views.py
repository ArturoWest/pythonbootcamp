from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse(content="To jest main page")

def hello_world(request):
    return HttpResponse(content="Hello World")

def hello_presonalized(request, name, lastname):
    return HttpResponse(content=f'Hello {name} / {lastname}')

