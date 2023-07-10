from django.urls import path

from . import views

urlpatterns = [
    # The 'home' parameter represents the DIR path we are taking to access
    #   the "views.py" file. As such, the parameter "views.home" points to
    #   the "home" FUNCTION inside that file.
    path('home', views.home)
]
