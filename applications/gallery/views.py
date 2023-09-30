from django.shortcuts import render
from django.views.generic import ListView
from .models import Image

# Create your views here.



class Gallery(ListView):
    model = Image
    template_name = "gallery/gallery.html"
