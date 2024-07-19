from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Version, Backup
from . import backup
import time

def releases(request):
    # 如果Backup为空或者最新的Backup距离现在大于5分钟，备份
    if Backup.objects.count() == 0 or (time.time() - Backup.objects.last().backup_time.timestamp() > 300):
        backup.get_release_info()
        Backup.objects.create(
            # 创建Backup的时间
            backup_time=time.localtime()
        )
    versions = Version.objects.all()
    for ver in versions:
        ver.description = ver.get_description()
    return render(request, 'download/releases.html', {'versions': versions})

def release(request, tag):
    target_ver = Version.objects.get(tag=tag)
    return render(request, 'download/release.html', {'target_ver': target_ver})
# 只有管理员可以访问
@permission_required('download.clear_cache')
def clear_cache(request):
    Backup.objects.all().delete()
    return redirect('download:releases')