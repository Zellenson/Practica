from django.shortcuts import render

def principal(request):
    return render(request, "inicio/principal.html")

# Create your views here.
