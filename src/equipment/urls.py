""" URLS """
from rest_framework.routers import DefaultRouter
from .viewsets import EquipmentsViewSet, VariablesViewSet

router = DefaultRouter()

router.register(r"equipments", EquipmentsViewSet)
router.register(r"variables", VariablesViewSet)

urlpatterns = router.urls
