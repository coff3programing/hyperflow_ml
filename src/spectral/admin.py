""" Admin """
from django.contrib import admin
from .models import (
    SpectralSignaturesUploadFiles,
    SpectralSignaturesData,
    SpectralSignaturesInfo
)

# Register your models here.

admin.site.register(SpectralSignaturesUploadFiles)
admin.site.register(SpectralSignaturesData)
admin.site.register(SpectralSignaturesInfo)
