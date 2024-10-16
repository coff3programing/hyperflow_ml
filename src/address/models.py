""" Address Model """
from django.db import models


class AddressModel(models.Model):
    """ Address Model """
    provincia = models.CharField(max_length=100)
    canton = models.CharField(max_length=100)
    parroquia = models.CharField(max_length=100)

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'address'
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self) -> str:
        """ String representation """
        return f"Parroquia: {self.parroquia}"


class UploadFilesModel(models.Model):
    """ Upload File """
    file = models.FileField(upload_to="address")

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'uploads'
        verbose_name = 'upload file'
        verbose_name_plural = 'upload files'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.file.name}"


class TeamsModels(models.Model):
    """ Team Model """
    team_name = models.CharField(max_length=100)
    team_lider_name = models.CharField(max_length=75)
    team_description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False, upload_to='teams')
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'teams'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.team_name} - {self.team_lider_name}"
