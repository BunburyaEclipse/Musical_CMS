import urllib.parse
from django.shortcuts import render
from django.views.generic import TemplateView

""" MODELOS """

from .models import Contact, News
from applications.gallery.models import Image
from applications.plans.models import Plan

###############

# Create your views here.

link_redes = []

def get_links():
    global link_redes
    links = []
    msg_redes = [
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_sing().name} con el valor de ${Plan.objects.get_sing().price} por favor 😄' if Plan.objects.get_sing() else ''),
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_piano().name} con el valor de ${Plan.objects.get_piano().price} por favor 😄' if Plan.objects.get_piano() else ''),
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_drumps().name} con el valor de ${Plan.objects.get_drumps().price} por favor 😄' if Plan.objects.get_drumps() else ''),
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_guitar().name} con el valor de ${Plan.objects.get_guitar().price} por favor 😄' if Plan.objects.get_guitar() else ''),
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_bass().name} con el valor de ${Plan.objects.get_bass().price} por favor 😄' if Plan.objects.get_bass() else ''),
        (f'Me gustaría preguntar más información sobre el curso de {Plan.objects.get_violin().name} con el valor de ${Plan.objects.get_violin().price} por favor 😄' if Plan.objects.get_violin() else ''),    ]

    for msg in msg_redes:
        quoted = urllib.parse.quote_plus(msg)
        link = Contact.objects.last().wa_link + quoted
        links.append(link)

    link_redes = links
    
    return link_redes




    # ###

    # 'descuento_canto': f'Me gustaria conseguir más información sobre el descuento {Plan.objects.get_sing.discount}',
    # 'descuento_piano': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_piano().name} con el vin',
    # 'descuento_bateria': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_drumps().name} con el vain',
    # 'descuento_guitarra': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_guitar().name} con el vain',
    # 'descuento_bajo': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_bass().name} con el in',
    # 'descuento_violin': f'Me gustaria preguntar más información sobre el curso de {Plan.objects.get_violin().name} con el vain',





class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        get_links()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['mensajes'] = {
            'canto': link_redes[0],
            'piano': link_redes[1],
            'bateria': link_redes[2],
            'guitarra': link_redes[3],
            'bajo': link_redes[4],
            'violin': link_redes[5],
        }
        return context
    

class about_us(TemplateView):
    template_name = "home/about_us.html"