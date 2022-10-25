from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Photo
from .serializers import PhotoSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def list_photos(request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)
