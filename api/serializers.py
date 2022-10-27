from rest_framework import serializers
from rest_framework.response import Response
from .models import Photo, PhotoFields

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
        fields = (PhotoFields.title, PhotoFields.albumId, PhotoFields.url)

    def save_photo(self):
        if not self.is_valid():
            return Response(data='Invalid request', status=400)

        # Loading image
        img = ImageParser.get_image(self.validated_data[PhotoFields.url])
        if img is None:
            return Response(data='Image can not be loaded. http/https missing?', status=400)

        # Removing previously loaded picture on Update request
        if self.instance is not None:
            ImageStorage.remove(self.instance.url)

        # Generating new url and saving it
        url = ImageStorage.generate_url(self.validated_data[PhotoFields.albumId])
        ImageStorage.save_image(img, Path(BASE_DIR, url))
        self.validated_data[PhotoFields.url] = url.as_posix()

        # Calculating width, height and dominating color
        params = ImageParser.get_image_info(img)
        for field in (PhotoFields.width, PhotoFields.height, PhotoFields.dominant_color):
            self.validated_data[field] = params[field]

        save = self.save()
        output = OutputPhotoSerializer(save)
        return Response(output.data, status=200)
