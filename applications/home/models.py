from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import NewsManager

# Create your models here.

class News(models.Model):
    title = models.CharField("Titulo", max_length=30, blank=False, null=False)
    content = models.TextField("Contenido", max_length=130, blank=False, null=False)
    pub_date = models.DateTimeField("Fecha de publicacion", default=timezone.now, blank=True, null=False, editable=False)
    objects = NewsManager()


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
    andress = models.TextField("Dirección", blank=False, null=False, max_length=350)

    @property
    def phone_format(self):
        numb = str(self.phone)
        return f"{numb[:4]} {numb[4:6]} {numb[6:9]} {numb[9:]}"

    def save(self, *args, **kwargs):
        if not self.whatsapp:
            self.whatsapp = f'https://wa.me/{self.phone}'
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        