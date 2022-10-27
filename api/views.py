from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import Photo, PhotoFields
from .serializers import InputPhotoSerializer, OutputPhotoSerializer
from data_import.json_importer import JSONImporter
from storage.image_storage import ImageStorage


@api_view(['GET'])
def api_overview(_):
    api_urls = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<int:pk>/',
        'Delete': '/delete/<int:pk>/',
        'Import from API': '/import/from_api/',
        'Import from file': '/import/from_file/'
    }
    return Response(api_urls)


@api_view(['GET'])
def list_photos(_):
    photos = Photo.objects.all()
    serializer = OutputPhotoSerializer(photos, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_photo(request):
    """
    Parses a photo from given URL, saves it at albumId folder.

    {
    <str:title>
    <int:albumId>
    <str:url>
    }
    """
    serializer = InputPhotoSerializer(data=request.data)
    return serializer.save_photo()


@api_view(['POST'])
def update_photo(request, pk):
    """
    Updates a photo, moves it to a different album and saves current URL.

    {
    <str:title>
    <int:albumId>
    <str:url>
    }
    """
    photo = Photo.get_by_id(pk)
    if not photo:
        return Response(f'Photo by id={pk} is not found', status=404)

    serializer = InputPhotoSerializer(instance=photo, data=request.data)
    return serializer.save_photo()


@api_view(['DELETE'])
def delete_photo(_, pk):
    """
    Parses a photo with given primary key.

    {
    <int:pk>
    }
    """
    photo = Photo.get_by_id(pk)
    if not photo:
        return Response(f'Photo by id={pk} is not found', status=404)

    ImageStorage.remove(photo.url)
    photo.delete()
    return Response(status=200)


@api_view(['POST'])
def import_from_api(request):
    """
    Imports multiple photos from a third-party API.

    [*{
    <str:title>
    <int:albumId>
    <str:url>
    }]
    """
    url = request.data.get(PhotoFields.url)
    if not url:
        Response('Invalid URL', status=400)

    return JSONImporter.import_from_url(url)


@api_view(['POST'])
@parser_classes((MultiPartParser, JSONParser))
def import_from_file(request):
    """
    Imports multiple photos from a JSON file.
    File is sent via multipart/form-data.

    [*{
    <str:title>
    <int:albumId>
    <str:url>
    }]
    """
    file = request.FILES.get(PhotoFields.file)
    if not file:
        return Response(f'{PhotoFields.file} attribute is not provided', status=400)

    return JSONImporter.import_from_file(file)
