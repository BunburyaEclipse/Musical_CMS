from django.urls import path, re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

app_name = "home"

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]