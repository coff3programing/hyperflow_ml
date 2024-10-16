""" DB """
from django.db import models

# Create your models here.


class ErrorsModel(models.Model):
    """ Errors model. """
    error_name = models.CharField(max_length=75)

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    db_table = 'errors'
    verbose_name = 'Error'
    verbose_name_plural = 'Errors'

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.error_name}"


class AnomaliesModel(models.Model):
    """ Anomalos model. """
    atypical_measurement_number = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='anomalos')
    errors = models.ForeignKey(ErrorsModel, on_delete=models.CASCADE)
    error_description = models.CharField(max_length=150,
                                         null=True, blank=True)

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    db_table = 'anomalies'
    verbose_name = 'Anomalie'
    verbose_name_plural = 'Anomalies'

    def __str__(self) -> str:
        return f"{self.atypical_measurement_number} - {self.errors}"
