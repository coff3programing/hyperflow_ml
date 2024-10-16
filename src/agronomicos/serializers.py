""" Parsers for agronomicos app """
import os
import uuid
from rest_framework import serializers
from .models import UploadAgronomicosFilesModel


class UploadFileSerializer(serializers.ModelSerializer):
    """ Upload Settings """
    class Meta:
        """ Settings for model"""
        model = UploadAgronomicosFilesModel
        fields = ['levels', 'file', 'file_name', 'created_at', 'updated_at']

    def create(self, validated_data):
        """Rename the file if a file_name is provided."""
        file = validated_data.get('file')
        file_name = validated_data.get('file_name')

        # Rename the file if a new file_name is provided
        if file_name:
            self._rename_file(file, file_name)
        return super().create(validated_data)

    def _rename_file(self, file, file_name):
        """Rename file by preserving its original extension."""
        _, ext = os.path.splitext(file.name)
        unique_id = uuid.uuid4()
        file.name = f'{file_name}{unique_id}{ext}'
