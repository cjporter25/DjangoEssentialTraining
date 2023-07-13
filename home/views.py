from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

# The function "home" receives a request
def home(request):
    # Returns an HttpResponse containing the string "Hello World"
    # return HttpResponse('Hello, world!')
    # The more common thing is to use the built in "render" function to 
    #   return a specific html view. The parameter should have the full
    #   necessary folder hierarchy for reference.
    # The "{}" parameter allows the user to pass in any information they'd 
    #   like. The target template must include a variable that can recieve
    #   this input
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    # This function is similar to the above "home" function that renders and
    #   returns the welcome.html page. 
    # This function instead returns the authorized.html page.
    return render(request, 'home/authorized.html', {})