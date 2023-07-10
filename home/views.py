from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# The function "home" receives a request
def home(request):
    # Returns an HttpResponse containing the string "Hello World"
    return HttpResponse('Hello, world!')
