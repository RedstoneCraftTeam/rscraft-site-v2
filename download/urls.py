from . import views
from django.urls import path
app_name = 'download'
urlpatterns = [
    path('<tag>/', views.release, name='release'),
    path('', views.releases, name='releases'),
    path('clear_cache', views.clear_cache, name='clear_cache'),
]
