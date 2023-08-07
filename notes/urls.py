from django.urls import path

# From the current directory, import the views.py file
from . import views

# Create a urlpatterns object to establish URL paths for notes -->
urlpatterns = [
    # Class based implementation
    # NOTE: Adding the parameter "name" allows the developer to establish a naming convention for
    #       URL redirects. See "welcome.html" in the home app.
    path('notes', views.NotesListView.as_view(), name="notes.list"), 

    # The current path indicates we have a function called "list" in views that 
    #   should be activated.
    #           path('notes', views.list), 
    # This URL will receive a new value called "pk" with type "int" to indicate that 
    #   this value can contain a variety of 
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail")

]