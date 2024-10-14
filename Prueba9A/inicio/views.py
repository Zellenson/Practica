from django.shortcuts import render

def principal(request):
    return render(request, "inicio/principal.html")

def registrar(request):
    return render(request, "inicio/registrar.html")

# Create your views here.
