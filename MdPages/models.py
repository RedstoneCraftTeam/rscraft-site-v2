from django.db import models

# Create your models here.
class MarkdownFile(models.Model):
    page_name = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='markdown_files/')