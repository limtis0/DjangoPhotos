from django.urls import path
from . import views


class URL:
    API_DIR = '/api/'
    LIST = 'list/'
    CREATE = 'create/'
    UPDATE = 'update/'
    DELETE = 'delete/'
    IMPORT_API = 'import/from_api/'


urlpatterns = [
    path('', views.api_overview, name='API overview'),
    path(URL.LIST, views.list_photos, name='Photos list'),
    path(URL.CREATE, views.create_photo, name='Add photo'),
    path(f'{URL.UPDATE}<str:pk>/', views.update_photo, name='Update photo'),
    path(f'{URL.DELETE}<str:pk>/', views.delete_photo, name='Delete photo'),
    path(URL.IMPORT_API, views.import_from_api, name='Import from API')
]
