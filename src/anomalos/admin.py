""" Admin """
from django.contrib import admin
from .models import ErrorsModel, AnomaliesModel

# Register your models here.

admin.site.register(ErrorsModel)
admin.site.register(AnomaliesModel)
