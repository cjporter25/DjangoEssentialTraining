from django.shortcuts import render
from django.http import Http404

# Built in view types Django can use to query and list database objects
from django.views.generic import DetailView, ListView

# This import statement specifies that we are importing the 
#   class "Notes" from the python file "models" in the same directory
from .models import Notes

# Similar to the class creation in home/views.py, we do the same here.
#   Class: NotesListView
#   Inherits From: ListView
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

#### NO LONGER NEEDED DUE TO THE ABOVE CLASS IMPLEMENTATION ####
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})
# Function - list(req)
# Usage - Take in a request and return all note objects fromn the database
#   Create a variable and save a call to all notes objects
#   Return a render that specifies the target template HTML file. The second parameter
#       again, allows the user to pass in specific information, i.e., a list of all note
#       objects.
# NOTE: Remember that the target HTML file must include the same variable name so that
#       it can actually receive the input
   
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # NOTE: DetailView class takes care of the error catching that we manually coded 
    #       originally in the function below

#### NO LONGER NEEDED DUE TO THE ABOVE CLASS IMPLEMENTATION ####
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
# Function - detail(req, pk)
# Usage - Retrieve a specific note object from the database based on an 
#         input pk (private key)
#   Try retrieving the object
#       If the specified object doesn't exist, raise an Http404 error.
#       If found, return a render of a different template, but pass in the 
#       local "note" object created above
    
# NOTE: Because we are passing in another parameter, the urlpattern that points to this 
#       function will need to account for that.
