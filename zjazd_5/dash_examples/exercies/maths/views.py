from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math
# Create your views here.

def calculate(operation, arg_a, arg_b):
    result = None
    if operation == "add":
        result = arg_a + arg_b
    elif operation == "sub":
        result = arg_a - arg_b
    return results

def math_operations(request, operations, arg_a, arg_b):
    results = None
    Math.objects.create(operations=operations, arg_a=arg_a, arg_b=arg_b)

    return HttpResponse(calculate(operation, arg_a, arg_b))

def math_list(request):
    objects = Math.objects.all()
    out = ""
    for o in objects:
        out += f"{o.operation}: {o.arg_a} {o.arg_b} <br>"
    return HttpResponse(out)

def math_details(request, id):
    m = Math.objects.get(pk=id)

    out = f"""
    Operacja: {m.operation)<br>
    arg 1: {m.arg_a}<br>
    arg 2: {m.arg_b}<br>
    ________________<br>
    Wynik: {calculate{m.operation, m.arg_a, m.arg_b}<br>
    """
    return Httpresponse(out)