from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app1/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def ycy(request):
    return HttpResponse("Hello, ycy!")

def greet(request, name):
    return render(request, "app1/greet.html", {
        "name": name.capitalize()
    })