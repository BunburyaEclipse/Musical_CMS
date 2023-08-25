from django.shortcuts import render
from django.views.generic import TemplateView

""" MODELOS """

from .models import Contact, News
from applications.gallery.models import Image
from applications.plans.models import Plan

###############

# Create your views here.


class Prueba(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['contacto'] = Contact.objects.last()
        context['noticias'] = News.objects.get_last_news
        context['imagenes'] = Image.objects.gallery_home
        context['instrumentos'] = {
            'piano': Plan.objects.get_piano(),
            'guitar': Plan.objects.get_guitar(),
            'bass': Plan.objects.get_bass(),
            'drumps': Plan.objects.get_drumps(),
            'violin': Plan.objects.get_violin(),
            'sing': Plan.objects.get_sing()
        }
        return context