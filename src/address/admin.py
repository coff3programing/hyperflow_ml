""" Admin """
from django.contrib import admin
from .models import AddressModel, TeamsModels, UploadFilesModel

# Register your models here.
admin.site.register(AddressModel)
admin.site.register(TeamsModels)
admin.site.register(UploadFilesModel)
