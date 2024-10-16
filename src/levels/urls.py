""" Address URL Configuration """
from django.urls import path
from .viewsets import LevelsViewSet, ListLevelsViewSet
from .views import UploadLevelsView

prefix: str = "levels"

urlpatterns = [
    path(f"{prefix}/upload/", UploadLevelsView.as_view()),
    path(f"{prefix}/info/", ListLevelsViewSet.as_view()),
    path(f"{prefix}/<int:pk>/", LevelsViewSet.as_view()),
]
