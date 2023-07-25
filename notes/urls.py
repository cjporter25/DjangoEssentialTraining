from django.urls import path

# From the current directory, import the views.py file
from . import views

# Create a urlpatterns object to establish URL paths for notes -->
urlpatterns = [
    # The current path indicates we have a function called "list" in views that 
    #   should be activated.
    path('notes', views.list), 
    # This URL will receive a new value called "pk" with type "int" to indicate that 
    #   this value can contain a variety of 
    path('notes/<int:pk>', views.detail)

]