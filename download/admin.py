from django.contrib import admin
from .models import Version, Backup

# Register your models here.
admin.site.register(Version)
admin.site.register(Backup)