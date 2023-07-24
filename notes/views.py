from django.shortcuts import render

# This import statement specifies that we are importing the 
#   class "Notes" from the python file "models" in the same directory
from .models import Notes

# This file is where "views" or "templates" are created for an app

# Function - list()
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
