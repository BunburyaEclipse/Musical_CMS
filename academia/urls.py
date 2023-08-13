"""
URL configuration for academia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name='home:prueba')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


applications_url = [
    path("home/", include("applications.home.urls", namespace="home")),
    path("gallery/", include("applications.gallery.urls", namespace="gallery")),
    path("videos/", include("applications.videos.urls", namespace="videos")),
    path("plans/", include("applications.plans.urls", namespace="plans")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns.extend(applications_url)