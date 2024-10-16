""" URLS """
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import UploadAgronomicosFilesView
from .views import download_file_by_name

router = DefaultRouter()

router.register(r"agronomicos", UploadAgronomicosFilesView)

prefix: str = "agronomicos"

urlpatterns = [
    path("", include(router.urls)),
    path(f"{prefix}/download/<str:file_name>/", download_file_by_name)
]
