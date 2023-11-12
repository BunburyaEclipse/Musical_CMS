from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Image
# Create your views here.



class Gallery(ListView):
    context_object_name = "imagenes"
    model = Image
    template_name = "gallery/gallery.html"


class ImageDetail(DetailView):
    model = Image
    context_object_name = "imagen"
    template_name = "gallery/Image_Details.html"
