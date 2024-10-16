""" Admin """
from django.contrib import admin
from .models import EquipmentModel, VariablesModels

# Register your models here.

admin.site.register(EquipmentModel)
admin.site.register(VariablesModels)
