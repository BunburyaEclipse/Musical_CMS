import urllib.parse
from django.shortcuts import render
from django.views.generic import TemplateView

""" MODELOS """

from .models import Contact, News
from applications.gallery.models import Image
from applications.plans.models import Plan

###############

# Create your views here.

# whatsapp = f'{Contact.objects.last().whatsapp}?text='

# msg_redes = {
#     'canto': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_sing().name} con el valor de ${Plan.objects.get_sing().price} por favor 😄',
#     'piano': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_piano().name} con el valor de ${Plan.objects.get_piano().price} por favor 😄',
#     'bateria': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_drumps().name} con el valor de ${Plan.objects.get_drumps().price} por favor 😄',
#     'guitarra': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_guitar().name} con el valor de ${Plan.objects.get_guitar().price} por favor 😄',
#     'bajo': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_bass().name} con el valor de ${Plan.objects.get_bass().price} por favor 😄',
#     'violin': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_violin().name} con el valor de ${Plan.objects.get_violin().price} por favor 😄',

#     ###

#     'descuento_canto': f'Me gustaria conseguir más información sobre el descuento {Plan.objects.get_sing.discount}',
#     'descuento_piano': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_piano().name} con el vin',
#     'descuento_bateria': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_drumps().name} con el vain',
#     'descuento_guitarra': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_guitar().name} con el vain',
#     'descuento_bajo': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_bass().name} con el in',
#     'descuento_violin': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_violin().name} con el vain',
# }

class HomeView(TemplateView):
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