""" Address URL Configuration """
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UpladExcelView
from .viewsets import AddressViewSet, TeamsViewSet

router = DefaultRouter()
router.register(r"address", AddressViewSet)
router.register(r"teams", TeamsViewSet)

prefix: str = "address"

urlpatterns = [
    path("", include(router.urls)),
    path(f"upload/{prefix}/", UpladExcelView.as_view()),
    path(f"{prefix}/parroquia/<str:parroquia_name>", UpladExcelView.as_view()),
]
