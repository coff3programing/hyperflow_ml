""" Admin """
from django.contrib import admin
from .models import LevelsModel, LevelsUploadFilesModel

# Register your models here.

admin.site.register(LevelsModel)
admin.site.register(LevelsUploadFilesModel)
