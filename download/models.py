from django.db import models

# Create your models here.
class Version(models.Model):
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    github_release = models.URLField()
    github_download_link = models.URLField()
    lanzou_url = models.URLField()
    
    def __str__(self):
        return self.tag + " - " + self.title
    
class Backup(models.Model):
    backup_time = models.DateTimeField(auto_now_add=True)