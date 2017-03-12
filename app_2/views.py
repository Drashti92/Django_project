from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! <em>This is my second project in python </em>")
