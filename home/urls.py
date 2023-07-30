from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.home),
    #   The 'home' parameter represents the DIR path we are taking to access
    #       the "views.py" file. As such, the parameter "views.home" points to
    #       the "home" FUNCTION inside that file.

    path('home', views.HomeView.as_view()),
        # NOTE: Class based option. We had to change the target element within
        #       "views.py" to the HomeView class rather than the 'home' function
    path('authorized', views.AuthorizedView.as_view()),
]
