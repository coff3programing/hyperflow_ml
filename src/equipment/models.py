""" DB Equipments """
from django.db import models
from src.address.models import TeamsModels

# Create your models here.


class VariablesModels(models.Model):
    """ Variables Model """
    variables_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    db_table = 'variables'
    verbose_name = 'Variable'
    verbose_name_plural = 'Variables'

    def __str__(self) -> str:
        return f"{self.variables_name}"


class EquipmentModel(models.Model):
    """ Equipment model. """
    team = models.ForeignKey(TeamsModels, on_delete=models.CASCADE)
    computer_name = models.CharField(max_length=100)
    initial_spectral_range = models.PositiveIntegerField()
    final_spectral_range = models.PositiveIntegerField()
    serie_number = models.CharField(max_length=100)
    bandwidth = models.FloatField(default=0)
    calibration_date = models.DateField()
    variable = models.ForeignKey(VariablesModels, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    db_table = 'equipments'
    verbose_name = 'Equipo'
    verbose_name_plural = 'Equipos'

    def __str__(self) -> str:
        return f"{self.computer_name}"
