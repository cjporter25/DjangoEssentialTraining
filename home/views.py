from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView #Class based views
# from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

# NOTE: CLASS BASED VARIANT
# Class - "HomeView"
# Inherits From = "TemplateView"
class HomeView(TemplateView):
    
    # Extra data to import into the template view
    extra_content = {'today': datetime.today()}
    # Target Template
    template_name = 'home/welcome.html'

# NOTE: NO LONGER NEEDED GIVEN ABOVE CLASS IMPLEMENTATION
# def home(request):
#   return render(request, 'home/welcome.html', {'today': datetime.today()})
#
# The function "home" receives a request
#   The following returns an HttpResponse containing the string "Hello World"
#       return HttpResponse('Hello, world!')
#   The more common thing is to use the built in "render" function to 
#       return a specific html view. The parameter should have the full
#       necessary folder hierarchy for reference.
#   The "{}" parameter allows the user to pass in any information they'd 
#       like. The target template must include a variable that can recieve
#       this input

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    # extra content variable not needed
    login_url = '/admin'

# NOTE: NO LONGER NEEDED GIVEN ABOVE CLASS IMPLEMENTATION
# @login_required(login_url='/admin')
# def authorized(request):
      # This function is similar to the above "home" function that renders and
      #   returns the welcome.html page. 
      # This function instead returns the authorized.html page.
      # return render(request, 'home/authorized.html', {})