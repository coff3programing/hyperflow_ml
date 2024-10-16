""" Parsers """
from rest_framework import serializers
from .models import ErrorsModel, AnomaliesModel


class ErrorSerializers(serializers.ModelSerializer):
    """ Errors """
    class Meta:
        """ Errors """
        model = ErrorsModel
        fields = '__all__'


class AnomalieSerializer(serializers.ModelSerializer):
    """ Anomalies """
    class Meta:
        """ Errors """
        model = AnomaliesModel
        fields = '__all__'
