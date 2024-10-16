""" URLS """
from rest_framework.routers import DefaultRouter
from .viewsets import AnomaliesView, ErrorView

router = DefaultRouter()

router.register(r"anomalies", AnomaliesView)
router.register(r"errors", ErrorView)

urlpatterns = router.urls
