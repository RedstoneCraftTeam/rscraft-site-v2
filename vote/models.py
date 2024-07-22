from django.db import models

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=100)
    vts_file = models.FileField(upload_to='vts_files/')