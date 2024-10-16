""" Parsers """
from datetime import datetime
from rest_framework import serializers
from .models import (
    SpectralSignaturesUploadFiles,
    SpectralSignaturesData,
    SpectralSignaturesInfo
)


class SpectralUploadFilesSerializer(serializers.ModelSerializer):
    """ Serializer for upload files """
    file = serializers.FileField()

    class Meta:
        """ Settings for model """
        model = SpectralSignaturesUploadFiles
        fields = ['file', 'created_at', 'updated_at']

    def validate_file(self, value):
        """ Validate file """
        # Obtiene el nombre del archivo
        filename = value.name

        # Verifica la extensión del archivo
        if not filename.endswith(('.txt', '.sed')):
            raise serializers.ValidationError(
                'Only .txt and .sed files are allowed.'
            )

        return value


class SpectralDataSerializer(serializers.ModelSerializer):
    """ Serializer for data """

    class Meta:
        """ Settings for model """
        model = SpectralSignaturesData
        fields = '__all__'


class CustomDateField(serializers.DateField):
    """ Custom date field """
    def to_representation(self, value):
        if isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%d').date()
        return value.strftime('%m-%d-%Y') if value else None

    def to_internal_value(self, data):
        try:
            # Cambia el formato de MM-DD-YYYY a YYYY-MM-DD
            date_obj = datetime.strptime(data, '%Y-%m-%d')
            return date_obj.date()
        except ValueError:
            self.fail('invalid_date_format', format='YYYY-MM-DD')


class SpectralInfoSerializer(serializers.ModelSerializer):
    """ Serializer for info """
    initial_date = CustomDateField()
    end_date = CustomDateField()
    initial_time = serializers.TimeField()
    end_time = serializers.TimeField()
    initial_temperature = serializers.FloatField()
    end_temperature = serializers.FloatField()
    initial_voltage = serializers.FloatField()
    end_voltage = serializers.FloatField()
    initial_averages = serializers.IntegerField()
    end_averages = serializers.IntegerField()

    class Meta:
        """ Settings for model """
        model = SpectralSignaturesInfo
        fields = '__all__'
