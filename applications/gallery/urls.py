from django.urls import path, re_path
from . import views

app_name = "galeria"

urlpatterns = [
    path("", views.Gallery.as_view(), name='gallery')
]