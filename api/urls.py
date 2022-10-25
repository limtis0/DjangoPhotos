from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='API Overview'),
    path('list/', views.list_photos, name='Photos List'),
]
