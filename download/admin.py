from django.contrib import admin
from .models import Version, Backup

def clear_versions(modeladmin, request, queryset):
    Version.objects.all().delete()
clear_versions.short_description = "Clear all Versions"

def clear_backups(modeladmin, request, queryset):
    Backup.objects.all().delete()
clear_backups.short_description = "Clear all Backups"

class VersionAdmin(admin.ModelAdmin):
    actions = [clear_versions]

class BackupAdmin(admin.ModelAdmin):
    actions = [clear_backups]

admin.site.register(Version, VersionAdmin)
admin.site.register(Backup, BackupAdmin)