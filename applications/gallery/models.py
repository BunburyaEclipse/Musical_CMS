from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from PIL import Image as PilImage
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import FileResponse

from applications.gallery.managers import HomeImagesManager

# Create your models here.

class Category(models.Model):
    name = models.CharField("Nombre de la categoria", max_length=50)

    def __str__(self):
        return self.name



def custom_image_name(instance, filename):
    # Obtiene la extensión del archivo original
    ext = "webp"
    if ext == "png" or ext == "jpg" or ext == "jpeg" or ext == "webp":
        # Genera un nuevo nombre para el archivo utilizando el ID del objeto y la extensión
        slugify_title = slugify(instance.titulo)
        pub_date_formatted = instance.pub_date.strftime('%Y-%m-%d')
        new_filename = f'-{slugify_title}-{pub_date_formatted}_{instance.id}.{ext}'
        # Devuelve la ruta completa del archivo
        return os.path.join('images/', new_filename)
    else:
        raise ValidationError("Formato de imagen no valido")


class Image(models.Model):
    titulo = models.CharField()
    slug = models.SlugField(unique=True, blank=True, editable=False)
    image = models.ImageField(upload_to=custom_image_name, blank=False)
    pub_date = models.DateTimeField("Fecha de publicacion", default=timezone.now, blank=True, null=False, editable=False)
    public = models.BooleanField("Publico", default=False)
    principal = models.BooleanField("Visible en la pantalla principal", default=False)
    category = models.ManyToManyField(Category, related_name='Imagenes')

    objects = HomeImagesManager()

    def __str__(self):
        return f"{self.titulo}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.titulo}-{self.pk}-{self.pub_date}")
        super().save(*args, **kwargs)


def optimize_image(sender, instance, **kwargs):
    with PilImage.open(instance.image.path) as img:
        img.convert("RGB")
        print(instance.image.path)
        img.save(instance.image.path, format="WEBP", optimize=True, quality=50)



post_save.connect(optimize_image, sender=Image)