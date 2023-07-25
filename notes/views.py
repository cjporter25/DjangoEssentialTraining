from django.shortcuts import render
from django.http import Http404

# This import statement specifies that we are importing the 
#   class "Notes" from the python file "models" in the same directory
from .models import Notes

# This file is where "views" or "templates" are created for an app

# Function - list(req)
# Usage - Take in a request and return all note objects fromn the database
def list(request):
    # Create a variable and save a call to all notes objects
    all_notes = Notes.objects.all()
    # Return a render that specifies the target template HTML file. The second parameter
    #   again, allows the user to pass in specific information, i.e., a list of all note
    #   objects.
    # NOTE: Remember that the target HTML file must include the same variable name so that
    #       it can actually receive the input
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

# Function - detail(req, pk)
# Usage - Retrieve a specific note object from the database based on an 
#         input pk (private key)
def detail(request, pk):
    # Try retrieving the object
    try:
        note = Notes.objects.get(pk=pk)
    # If the specified object doesn't exist, raise an Http404 error.
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
        # Return a render of a different template, but pass in the local "note" 
        #   object created above
    return render(request, 'notes/notes_detail.html', {'note': note})
    # NOTE: Because we are passing in another parameter, the urlpattern that points to this 
    #       function will need to account for that.
