from django.shortcuts import render
from .models import Version
# Create your views here.
def releases(request):
    versions = Version.objects.all()
    return render(request, 'download/releases.html', {'versions': versions})

def release(request, tag):
    target_ver = Version.objects.get(tag=tag)
    return render(request, 'download/release.html', {'target_ver': target_ver})