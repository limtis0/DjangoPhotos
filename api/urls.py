from django.urls import path
from . import views


class URL:
    API_DIR = '/api/'
    LIST = 'list/'
    CREATE = 'create/'
    UPDATE = 'update/'
    DELETE = 'delete/'


urlpatterns = [
    path('', views.api_overview, name='API Overview'),
    path(URL.LIST, views.list_photos, name='Photos List'),
    path(URL.CREATE, views.create_photo, name='Add Photo'),
    path(f'{URL.UPDATE}<str:pk>/', views.update_photo, name='Update Photo'),
    path(f'{URL.DELETE}<str:pk>/', views.delete_photo, name='Delete Photo')
]
