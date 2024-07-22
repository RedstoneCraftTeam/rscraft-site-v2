from . import views
from django.urls import path
app_name = 'votes'
urlpatterns = [
    path('<vote_name>/', views.vote_page, name='vote'),
    path('', views.vote_list, name='votes'),
    path('<vote_name>/<select_id>', views.submit, name='vote_selected')
]
