""" Parsers """
import os
from rest_framework import serializers
from .models import LevelsModel, LevelsUploadFilesModel


class LevelsSerializer(serializers.ModelSerializer):
    """ Levels """
    class Meta:
        """ Meta """
        model = LevelsModel
        fields = '__all__'


class LevelsUploadFilesSerializer(serializers.ModelSerializer):
    """ Levels """
    class Meta:
        """ Meta """
        model = LevelsUploadFilesModel
        fields = '__all__'

        def validate_file(self, value):
            """ Validate file """
            ext = os.path.splitext(value.name)[1]
            valid_extensions = ['.xlsx', '.xls']

            if ext not in valid_extensions:
                raise serializers.ValidationError(
                    'Unsupported file extension.'
                )

            return value
