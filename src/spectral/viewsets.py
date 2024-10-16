""" ViewSets😜 """
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import SpectralDataSerializer, SpectralInfoSerializer
from .models import SpectralSignaturesData, SpectralSignaturesInfo


class ListSpectarlInfoViewSet(ListAPIView):
    """ Detail Spectral Info ViewSet """
    allowed_methods = ["GET"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SpectralInfoSerializer
    queryset = SpectralSignaturesInfo.objects.all()


class ListSpectralDataViewSet(ListAPIView):
    """ Spectral Data ViewSet """
    allowed_methods = ["GET"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SpectralDataSerializer
    queryset = SpectralSignaturesData.objects.all()


class SpectralDataViewSet(RetrieveAPIView):
    """ Spectral Data ViewSet """
    allowed_methods = ["GET", "PUT", "DELETE"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SpectralDataSerializer
    queryset = SpectralSignaturesData.objects.all()


class SpectarlInfoViewSet(RetrieveAPIView):
    """ Detail Spectral Info ViewSet """
    allowed_methods = ["GET", "PUT", "DELETE"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = SpectralInfoSerializer
    queryset = SpectralSignaturesInfo.objects.all()
