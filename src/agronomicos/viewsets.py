""" Viewsets for agronomicos app """
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UploadAgronomicosFilesModel
from .serializers import UploadFileSerializer

# Create your views here.


class UploadAgronomicosFilesView(viewsets.ModelViewSet):
    """ Viewsets for agronomicos app """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = UploadAgronomicosFilesModel.objects.all()
    serializer_class = UploadFileSerializer
