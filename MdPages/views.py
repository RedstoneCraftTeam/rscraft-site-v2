from django.shortcuts import render
from .models import MarkdownFile
# Create your views here.
def page(request, page_name):
    selected_page = MarkdownFile.objects.get(page_name=page_name)
    file_content = selected_page.file_path.read().decode('utf-8')
    file_content = file_content.replace('\r\n', '\\n')
    return render(request, 'pages/page.html', {'page_name': page_name, 'file_content': file_content})