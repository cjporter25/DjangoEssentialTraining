from django.db import models

# Create your models here.
class Notes(models.Model):
# Think - What attributes should be a part of a note?
    # A "title" cannot have more than 200 characters
    title = models.CharField(max_length=200)
    # The "text" contains space in a textfield format
    text = models.TextField()
    # "Created" represents the date/time a Notes object was created.
    #   "auto_now_add=True" signals the function to automatically import 
    #   the current date and time from the system.
    created = models.DateTimeField(auto_now_add=True)
