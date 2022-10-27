from rest_framework import serializers
from rest_framework.response import Response
from .models import Photo

from pathlib import Path
from DjangoPhotos.settings import BASE_DIR
from storage.image_storage import ImageStorage
from data_import.image_parser import ImageParser


class OutputPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class InputPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'albumId', 'url')

    def save_photo(self):
        if not self.is_valid():
            return Response(data='Invalid form', status=400)

        # Loading image
        img = ImageParser.get_image(self.validated_data['url'])
        if not img:
            return Response(data='Image can not be loaded', status=400)

        # Removing previously loaded picture on update
        if self.instance is not None:
            ImageStorage.remove(self.instance.url)

        # Generating new url and saving it
        url = ImageStorage.generate_url(self.validated_data['albumId'])
        ImageStorage.save_image(img, Path(BASE_DIR, url))
        self.validated_data['url'] = url.as_posix()

        # Calculating width, height and dominating color
        params = Photo.get_image_info(img)
        self.validated_data['width'] = params['width']
        self.validated_data['height'] = params['height']
        self.validated_data['color'] = params['color']

        self.save()

        return Response(self.data, status=200)
