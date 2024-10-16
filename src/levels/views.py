""" Views """
import polars as pl
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .models import LevelsModel
from .serializers import LevelsUploadFilesSerializer


# Create your views here.


class UploadLevelsView(APIView):
    """ Upload Levels """
    allowed_methods = ['POST']
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        """ Upload File """
        serializer = LevelsUploadFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excel_file = serializer.save()
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

        try:
            # * DF Polars
            df_levels = pl.read_excel(file_path, engine="openpyxl")

            # Verificar si hay al menos 10 columnas
            if df_levels.width < 10:
                return Response(
                    {
                        'error': 'El archivo debe tener al menos 10 columnas.'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Seleccionar las primeras 10 columnas
            df_levels = df_levels.select(df_levels.columns[:10])

            # Eliminar nulos y duplicados
            df_levels = df_levels.drop_nulls().unique()

            # 3 Cargar registros en la base de datos
            def add_data(record):
                """ Add Data """
                return LevelsModel.objects.create(
                    sublevel_one=record[df_levels.columns[0]],
                    sublevel_two=record[df_levels.columns[1]],
                    sublevel_three=record[df_levels.columns[2]],
                    sublevel_four=record[df_levels.columns[3]],
                    sublevel_five=record[df_levels.columns[4]],
                    sublevel_six=record[df_levels.columns[5]],
                    sublevel_seven=record[df_levels.columns[6]],
                    sublevel_eight=record[df_levels.columns[7]],
                    sublevel_nine=record[df_levels.columns[8]],
                    sublevel_ten=record[df_levels.columns[9]],
                )
            # 4 Llenando la DB con map
            list(map(add_data, df_levels.rows(named=True)))

            return Response(
                {"message": "Datos guardados exitosamente."},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

