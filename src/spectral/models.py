""" DB """
from django.contrib.postgres.fields import ArrayField
from django.db import models
from src.levels.models import LevelsModel

# Create your models here.


class SpectralSignaturesUploadFiles(models.Model):
    """ Model for upload files """
    file = models.FileField(upload_to="spectral_signatures")

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'uploads_spectral_signatures'
        verbose_name = 'Spectral Signature'
        verbose_name_plural = 'upload files Spectral Signatures'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.file.name}"


class SpectralSignaturesData(models.Model):
    """Model for spectral signatures data"""
    levels = models.ForeignKey(LevelsModel, on_delete=models.CASCADE,
                               blank=True, null=True)
    x = ArrayField(models.FloatField(default=0.0), blank=True)
    y = ArrayField(models.FloatField(default=0.0), blank=True)

    class Meta:
        """ Settings for model """
        db_table = 'spectral_signatures_data'
        verbose_name = 'Spectral Signature Data'
        verbose_name_plural = 'Spectral Signatures Data'


class SpectralSignaturesInfo(models.Model):
    """Model for spectral signatures information"""
    initial_date = models.DateField()
    end_date = models.CharField(max_length=15, blank=True, null=True)
    initial_time = models.CharField(max_length=15, blank=True, null=True)
    end_time = models.TimeField()
    initial_temperature = models.FloatField(default=0.0)
    end_temperature = models.FloatField(default=0.0)
    initial_voltage = models.FloatField(default=0.0)
    end_voltage = models.FloatField(default=0.0)
    initial_averages = models.PositiveIntegerField(default=0)
    end_averages = models.PositiveIntegerField(default=0)

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'spectral_signatures_info'
        verbose_name = 'Spectral Signature Information'
        verbose_name_plural = 'Spectral Signatures Informations'

    def __str__(self) -> str:
        """ String representation """
        return f"Empieza: {self.initial_date} - {self.initial_time}"
