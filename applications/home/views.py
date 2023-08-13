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
        context['contexto2'] = 'Este es el contexto 2'
        context['contexto3'] = 'Este es el contexto 3'

        return context