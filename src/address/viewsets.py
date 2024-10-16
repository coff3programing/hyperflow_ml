""" Viewsets for address app """
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from src.utils.has_permissions import get_permission_classes
from .models import AddressModel, TeamsModels
from .serializers import AddressSerializer, TeamsSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """ Viewset for address app """
    authentication_classes = [TokenAuthentication]
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer

    def get_permissions(self):
        permission_classes = get_permission_classes(self.action)
        # Devuelve las clases de permisos instanciadas
        return [permission() for permission in permission_classes]


class TeamsViewSet(viewsets.ModelViewSet):
    """ Viewset for teams app """
    authentication_classes = [TokenAuthentication]
    queryset = TeamsModels.objects.all()
    serializer_class = TeamsSerializer

    def get_permissions(self):
        permission_classes = get_permission_classes(self.action)
        return [permission() for permission in permission_classes]
