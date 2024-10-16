""" Serializers for address app"""
import os
from rest_framework import serializers
from .models import AddressModel, UploadFilesModel, TeamsModels


class AddressSerializer(serializers.ModelSerializer):
    """ Address Serializer """
    class Meta:
        """ Settings for serializer"""
        model = AddressModel
        fields = '__all__'


class UploadFileSerializer(serializers.ModelSerializer):
    """ Upload """
    class Meta:
        """ Upload Settings """
        model = UploadFilesModel
        fields = ['file']

    def validate_file(self, value):
        """ Validate file """
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.xlsx', '.xls']

        if ext not in valid_extensions:
            raise serializers.ValidationError('Unsupported file extension.')
        return value


class TeamsSerializer(serializers.ModelSerializer):
    """ Teams Serializer """
    class Meta:
        """ Settings for serializer """
        model = TeamsModels
        fields = '__all__'
