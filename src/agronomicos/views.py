""" File Service """
import os
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import UploadAgronomicosFilesModel


def download_file_by_name(request, file_name):
    """Download the most recent file that matches the provided file_name."""
    file_obj = UploadAgronomicosFilesModel.objects.filter(
        file__icontains=file_name).first()

    if not file_obj:
        return Response(
            {
                "error": "El archivo no existe."
            }, status=status.HTTP_404_NOT_FOUND
        )
    # Construye la ruta completa del archivo
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
              fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename={
                os.path.basename(file_path)}'
            return response
    else:
        return Response("El archivo no se encuentra en el servidor.")
