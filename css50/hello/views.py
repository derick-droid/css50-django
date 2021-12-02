from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


# returning html document
def first(request):
    return render(request, "hello/hello.html")
def html_greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })

# just returning normal response without html
def greet(request):
    return HttpResponse("hello programmer")

def derick(request):
    return HttpResponse("hello derrick")
def enock(request):
    return HttpResponse("hello enock gang!")
def all_greet(request, name):
    return HttpResponse(f"hello,  {name}")