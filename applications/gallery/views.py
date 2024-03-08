from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
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

class img_prueba(TemplateView):
    template_name = "gallery/image_test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagen'] = Image.objects.last()
        return context
    