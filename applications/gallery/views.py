from django.shortcuts import render
from django.views.generic import ListView
from .models import Image
# Create your views here.



class Gallery(ListView):
    context_object_name = "imagenes"
    model = Image
    template_name = "gallery/gallery.html"
