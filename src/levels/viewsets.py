""" API Viewsets """
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import LevelsModel
from .serializers import LevelsSerializer

# Create your views here.


class ListLevelsViewSet(ListAPIView):
    """ Detail patient queryset. """
    allowed_methods = ["GET"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = LevelsSerializer
    queryset = LevelsModel.objects.all()


class LevelsViewSet(RetrieveUpdateDestroyAPIView):
    """ Detail patient queryset. """
    allowed_methods = ["GET", "PUT", "DELETE"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = LevelsSerializer
    queryset = LevelsModel.objects.all()
