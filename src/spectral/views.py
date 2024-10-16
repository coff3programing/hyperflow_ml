""" Views """
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from src.utils.df_data_spectral import extract_x_y
from src.utils.df_info_spectral import process_file
from .models import SpectralSignaturesInfo, SpectralSignaturesData
from .serializers import SpectralUploadFilesSerializer


class SpectralUploadFileView(APIView):
    """ Upload File """
    allowed_methods = ['POST']
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        """ Upload File """
        serializer = SpectralUploadFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excel_file = serializer.save()

        # Obtener la ruta del archivo
        file_path = excel_file.file.path

        # ? Se subio el archivo
        if not file_path:
            return Response(
                {
                    'status': 400,
                    'message': 'No se encontro el archivo'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Procesar el archivo utilizando las funciones respectivas de utils
        try:
            df_info = process_file(file_path)
            x_data, y_data = extract_x_y(file_path)
        except ValueError as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

        # Verificamos que ambas listas tengan el mismo tamaño
        if len(x_data) != len(y_data):
            return Response(
                {
                    "error": "The lists of X and Y do not match in size."
                }, status=status.HTTP_400_BAD_REQUEST
            )

        # Función para preparar los datos
        def add_info_data(record):
            """ Agregar datos al modelo SpectralSignaturesInfo """
            return SpectralSignaturesInfo.objects.create(
                initial_date=record['InitialDate'],
                end_date=record['EndDate'],
                initial_time=record['InitialTime'],
                end_time=record['EndTime'],
                initial_temperature=record['InitialTemperature'],
                end_temperature=record['EndTemperature'],
                initial_voltage=record['InitialVoltage'],
                end_voltage=record['EndVoltage'],
                initial_averages=record['InitialAverages'],
                end_averages=record['EndAverages'],
            )

        def create_spectral_data(x_data, y_data):
            """ Crear datos en la base de datos """
            spectral_data = SpectralSignaturesData.objects.create(
                x=x_data,
                y=y_data
            )
            return {"x": spectral_data.x, "y": spectral_data.y}

        # Agregar los datos al modelo
        list(map(add_info_data, df_info.rows(named=True)))
        create_spectral_data(x_data, y_data)

        return Response(
                {"message": "Datos guardados exitosamente."},
                status=status.HTTP_201_CREATED
            )
