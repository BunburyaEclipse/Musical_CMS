from typing import Iterable, Optional
from django.db import models
from datetime import datetime
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class News(TimeStampedModel):
    title = models.CharField("Titulo", max_length=80, blank=False, null=False)
    content = models.TextField("Contenido", max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'



class Contact(models.Model):
    email = models.EmailField("Email", max_length=50)
    phone = PhoneNumberField(region='EC')
    facebook = models.URLField("Url de facebook", max_length=100)
    instagram = models.URLField("Url de instagram", max_length=100)
    tiktok = models.URLField("Url de tiktok", max_length=100)
    whatsapp = models.URLField("Url de whatsapp", blank=True, null=False)

    def save(self, *args, **kwargs):
        if self.whatsapp:
            self.whatsapp = f'https://wa.me/{self.phone}'
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        