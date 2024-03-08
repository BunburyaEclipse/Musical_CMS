from django.urls import path, re_path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.Gallery.as_view(), name='gallery'),
    path('test_images', views.img_prueba.as_view(), name='image_test'),
    path('pictures/<int:pk>/', views.ImageDetail.as_view(), name='image_detail'),
]