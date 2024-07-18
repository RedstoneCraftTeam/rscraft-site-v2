from django.shortcuts import render
from .models import Version, Backup
from . import backup
import time
# Create your views here.
def releases(request):
    # 如果Backup为空或者最新的Backup距离现在大于5分钟，备份
    # TODO: 增加第二个条件
    if Backup.objects.count() == 0 :
        backup.get_release_info()
        Backup.objects.create(
            # 创建Backup的时间
            backup_time=time.mktime(time.localtime())
        )
    versions = Version.objects.all()
    return render(request, 'download/releases.html', {'versions': versions})

def release(request, tag):
    target_ver = Version.objects.get(tag=tag)
    return render(request, 'download/release.html', {'target_ver': target_ver})