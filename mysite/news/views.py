from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello index")

def test(request):
    return HttpResponse("<h1>Hello test page</h1>")
