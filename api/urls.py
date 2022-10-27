from django.urls import path
from . import views


class URL:
    API_DIR = '/api/'
    LIST = 'list/'
    CREATE = 'create/'
    UPDATE = 'update/'
    DELETE = 'delete/'
    IMPORT_API = 'import/from_api/'
    IMPORT_FILE = 'import/from_file/'


urlpatterns = [
    path('', views.api_overview, name='API overview'),
    path(URL.LIST, views.list_photos, name='Photos list'),
    path(URL.CREATE, views.create_photo, name='Add photo'),
    path(f'{URL.UPDATE}<int:pk>/', views.update_photo, name='Update photo'),
    path(f'{URL.DELETE}<int:pk>/', views.delete_photo, name='Delete photo'),
    path(URL.IMPORT_API, views.import_from_api, name='Import from API'),
    path(URL.IMPORT_FILE, views.import_from_file, name='Import from file'),
]
