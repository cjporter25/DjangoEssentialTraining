from django.contrib import admin

# "." indicates to python to import from the current folder
# We import the file "models.py" because that's where our model is located
from . import models


# This folder is where you register your models.
# The "admin.py" file inside an app is where the user can decide
#   whether an app should be accessible inside the Django Console or not.

# Use a similar naming scheme based on original app name.
#   This class should inherit from the Django ModelAdmin class.
class NotesAdmin(admin.ModelAdmin):
    # Pass signifies that no other modifications should occur
    # pass

    # Since we want to have the console allow fo object name changes, we 
    #   can add an attirbute in this class to allow that
    list_display = ('title',)
        # NOTE a Tuple can contain only one item if there is a comma

# ACTUALLY REGISTER THAT THE "notes" model is attached to this "admin" model
admin.site.register(models.Notes, NotesAdmin)