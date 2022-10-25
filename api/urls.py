from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='API Overview'),
    path('list/', views.list_photos, name='Photos List'),
    path('create/', views.create_photo, name='Add Photo'),
    path('update/<str:pk>/', views.update_photo, name='Update Photo'),
    path('delete/<str:pk>/', views.delete_photo, name='Delete Photo')
]
