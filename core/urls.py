"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

prefix: str = "api/v1"

urlpatterns = [
    path(f"{prefix}/", include('src.register.urls')),
    path(f"{prefix}/", include('src.address.urls')),
    path(f"{prefix}/", include('src.agronomicos.urls')),
    path(f"{prefix}/", include("src.anomalos.urls")),
    path(f"{prefix}/", include("src.docs.urls")),
    path(f"{prefix}/", include("src.equipment.urls")),
    path(f"{prefix}/", include("src.levels.urls")),
    path(f"{prefix}/", include("src.spectral.urls")),
    path(f"{prefix}/admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
