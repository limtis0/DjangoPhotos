from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Photo
from .serializers import InputPhotoSerializer, OutputPhotoSerializer
from data_import.json_importer import JSONImporter


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<str:pk>',
        'Delete': '/delete/<str:pk>/',
        'Import from API': '/import/from_api'
    }
    return Response(api_urls)


@api_view(['GET'])
def list_photos(request):
    photos = Photo.objects.all()
    serializer = OutputPhotoSerializer(photos, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_photo(request):
    serializer = InputPhotoSerializer(data=request.data)
    return serializer.save_photo()


@api_view(['POST'])
def update_photo(request, pk):
    photo = Photo.get_by_id(pk)
    if not photo:
        return Response(status=404)

    serializer = InputPhotoSerializer(instance=photo, data=request.data)
    return serializer.save_photo()


@api_view(['DELETE'])
def delete_photo(request, pk):
    photo = Photo.get_by_id(pk)
    if not photo:
        return Response(status=404)

    photo.delete()
    return Response(status=200)


@api_view(['POST'])
def import_from_api(request):
    url = request.data.get('url')
    if not url:
        Response(status=400)

    return JSONImporter.import_from_url(url)
