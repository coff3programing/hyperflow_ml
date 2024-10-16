""" Parses """
from rest_framework import serializers
from .models import EquipmentModel, VariablesModels


class EquipmentSerializer(serializers.ModelSerializer):
    """ Equipment Serializer """

    class Meta:
        """ Config """
        model = EquipmentModel
        fields = '__all__'


class VariablesSerializer(serializers.ModelSerializer):
    """ Variables Serializer """

    class Meta:
        """ Config """
        model = VariablesModels
        fields = '__all__'
