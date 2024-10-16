""" Views """
import polars as pl
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from src.utils.has_permissions import get_permission_methods
from .models import AddressModel
from .serializers import AddressSerializer, UploadFileSerializer


class UpladExcelView(APIView):
    """ Upload Excel File """
    allowed_methods = ['GET', 'POST']
    parser_classes = [MultiPartParser]
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        """ function based on request method """
        permission_classes = get_permission_methods(self.request.method)
        return [permission() for permission in permission_classes]

    def get(self, request, parroquia_name: None):
        """ List Addresses """
        if parroquia_name:
            # Filtramos las parroquias por nombre
            parroquias = AddressModel.objects.filter(parroquia=parroquia_name)
            # Comprobamos si el QuerySet está vacío
            if not parroquias.exists():
                # Lanzamos un error 404 si no se encuentra la parroquia
                return Response(
                    {
                        'status': 404,
                        'message': 'Parroquia no encontrada'
                    }, status=status.HTTP_404_NOT_FOUND
                )
            serializer = AddressSerializer(parroquias, many=True)
            return Response(
                {
                    'status': 200,
                    'data': serializer.data
                }, status=status.HTTP_200_OK
            )

    def post(self, request):
        """ Upload File """
        serializer = UploadFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excel_file = serializer.save()
        file_path = excel_file.file.path

        # * DF Polars
        df = pl.read_excel(file_path, engine="openpyxl")

        # Columnas requeridas
        required_columns = ['Provincia', 'Canton', 'Parroquia']
        # Verifica si todas las columnas requeridas están presentes en el DF
        missing_columns = [
            col for col in required_columns if col not in df.columns
        ]
        if missing_columns:
            # Si faltan columnas, devuelve un error con las columnas que faltan
            return Response(
                {
                    "error": "Faltan las siguientes columnas",
                    "columns": missing_columns
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # filtra el DataFrame por las columnas requeridas
        df_filtered = df.select(required_columns)
        # 1. Eliminar valores nulos
        df_filtered = df_filtered.drop_nulls()
        # 2. Eliminar duplicados
        df_filtered = df_filtered.unique()

        # 3 Cargar registros en la base de datos
        def add_data(record):
            """ Add Data """
            AddressModel.objects.create(
                provincia=record['Provincia'],
                canton=record['Canton'],
                parroquia=record['Parroquia']
            )

        # 4 Llenando la DB con map
        list(map(add_data, df.rows(named=True)))

        return Response(
            {
                "message": "File Upload and Data Saved"
            }, status=status.HTTP_201_CREATED
        )
