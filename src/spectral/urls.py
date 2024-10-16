""" URLS """
from django.urls import path
from .views import SpectralUploadFileView
from .viewsets import (
    ListSpectarlInfoViewSet,
    SpectarlInfoViewSet,
    ListSpectralDataViewSet,
    SpectralDataViewSet
)

prefix: str = "spectral"

urlpatterns = [
    path(f"{prefix}/upload/", SpectralUploadFileView.as_view()),
    path(f"{prefix}/info/", ListSpectarlInfoViewSet.as_view()),
    path(f"{prefix}/info/<int:pk>/", SpectarlInfoViewSet.as_view()),
    path(f"{prefix}/data/", ListSpectralDataViewSet.as_view()),
    path(f"{prefix}/data/<int:pk>/", SpectralDataViewSet.as_view()),
]
