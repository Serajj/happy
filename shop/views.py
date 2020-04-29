from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("I am about page")

def contact(request):
    return HttpResponse("I am contact page")

def search(request):
    return HttpResponse("I am search page")

def tracker(request):
    return HttpResponse("I am tracker page")

def checkout(request):
    return HttpResponse("I am checkout page")

def productView(request):
    return HttpResponse("I am productView page")