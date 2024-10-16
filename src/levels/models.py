""" DB """
from django.db import models

# Create your models here.


class LevelsModel(models.Model):
    """ DB Levels """
    sublevel_one = models.CharField(max_length=100)
    sublevel_two = models.CharField(max_length=100)
    sublevel_three = models.CharField(max_length=100)
    sublevel_four = models.CharField(max_length=100)
    sublevel_five = models.CharField(max_length=100)
    sublevel_six = models.CharField(max_length=100)
    sublevel_seven = models.CharField(max_length=100)
    sublevel_eight = models.CharField(max_length=100)
    sublevel_nine = models.CharField(max_length=100)
    sublevel_ten = models.CharField(max_length=100)

    # * Additional fields
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    db_table = 'levels'
    verbose_name = 'level'
    verbose_name_plural = 'levels'


class LevelsUploadFilesModel(models.Model):
    """ Upload File """
    file = models.FileField(upload_to="address")

    # * Auditoría
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """ Settings for model """
        db_table = 'uploads_levels'
        verbose_name = 'upload levels'
        verbose_name_plural = 'upload levels'

    def __str__(self) -> str:
        """ String representation """
        return f"{self.file.name}"
