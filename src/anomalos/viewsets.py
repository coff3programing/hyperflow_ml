""" Views """
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import AnomaliesModel, ErrorsModel
from .serializers import AnomalieSerializer, ErrorSerializers

# Create your views here.


class AnomaliesView(viewsets.ModelViewSet):
    """ CRUD Operations """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = AnomaliesModel.objects.all()
    serializer_class = AnomalieSerializer


class ErrorView(viewsets.ModelViewSet):
    """ Erros Crud """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = ErrorsModel.objects.all()
    serializer_class = ErrorSerializers
