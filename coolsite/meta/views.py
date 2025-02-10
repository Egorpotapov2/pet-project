from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def home (request):
#     return HttpResponse("Привет, Meta!")


def home (request):
    return render(request, "meta/home.html")

def bd (request):
    return render(request, "meta/registr.html")

def hod (request):
    return render(request, 'meta/signin.html')


