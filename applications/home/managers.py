from django.db import models

class HomeImagesManager(models.Manager):
    def gallery_images_all(self):
        return self.filter(public=True).order_by("-pub_date")

    def gallery_home(self):
        return self.filter(public=True, principal=True).order_by("-pub_date")


class NewsManager(models.Manager):
    def get_last_news(self):
        return self.order_by('-pub_date')[:8]