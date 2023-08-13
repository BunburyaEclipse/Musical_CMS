from django.db import models
from django.utils import timezone
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeFramedModel

INSTRUMENTS_CHOICES = (
    (1, 'Piano'),
    (2, 'Canto'),
    (3, 'Guitarra'),
    (4, 'Batería'),
    (5, 'Violin')
)


# class Prueba(models.Model):
#     Modalidades_Choises = Choices('Online', 'Presencial', 'Curso')
#     modality = StatusField(choices_name='Modalidades_Choises')
#     instrument = models.SmallIntegerField(choices=INSTRUMENTS_CHOICES)
#     price = models.IntegerField()



class Discount(models.Model):
    title = models.CharField("Nombre del del descuento", max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    State_Choises = Choices('Valido', 'Invalido')
    state = StatusField(choices_name='State_Choises')
    inicio = models.DateField(default=timezone.now)
    final = models.DateField(default=timezone.now() + timezone.timedelta(days=10))

    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
    
    def __str__(self):
        if self.state:
            return f'{self.title} --- {self.price} --- [ ACTIVADO ]'
        return f'{self.title} --- {self.price} --- [ DESACTIVADO ]'
    

class Plan(models.Model):
    name = models.CharField("Nombre del plan", max_length=80)
    description = models.TextField("Descripcion del plan")
    instrument = models.SmallIntegerField(choices=INSTRUMENTS_CHOICES)
    Modalidades_Choises = Choices('Online', 'Presencial', 'Curso')
    modality = StatusField(choices_name='Modalidades_Choises')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True, related_name='planes')

    class Meta:
        verbose_name = 'Plan de estudio'
        verbose_name_plural = 'Planes de estudio'
    
    def __str__(self):
        return f'{self.name} --- {self.instrument} ${self.price}'