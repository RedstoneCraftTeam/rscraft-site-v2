from . import views
from django.urls import path
app_name = 'MdPages'
urlpatterns = [
    path('<page_name>', views.page, name='page')
]
