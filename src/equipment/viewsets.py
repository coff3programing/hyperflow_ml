""" Viewsets for equipment app """
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import VariablesModels, EquipmentModel
from .serializers import VariablesSerializer, EquipmentSerializer

# Create your views here.


class VariablesViewSet(viewsets.ModelViewSet):
    """ Variables Viewset """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = VariablesModels.objects.all()
    serializer_class = VariablesSerializer


class EquipmentsViewSet(viewsets.ModelViewSet):
    """ Equipments Viewset """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentSerializer
