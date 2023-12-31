"""
URL configuration for smartnotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Adding the "include" function to include url routing pathways from apps
from django.urls import path, include

# No longer needed as pathway was added to the home DIR directly
# from home import views 

urlpatterns = [
    path('admin/', admin.site.urls), # --> www.mywebsite.com/admin
    path('', include('home.urls')), # --> www.mywebsite.com/home
    path('smart/', include('notes.urls')), # --> www.mywebsite.com/smart/notes
]
