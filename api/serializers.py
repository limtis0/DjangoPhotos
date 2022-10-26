from rest_framework import serializers
from rest_framework.response import Response
from .models import Photo

from DjangoPhotos.settings import MEDIA_ROOT, MEDIA_URL
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

    def save_photo(self, driver=None):
        if not self.is_valid():
            return Response(data='Invalid form', status=400)

        close_driver = False
        if driver is None:
            driver = ImageParser.get_webdriver()
            close_driver = True

        # Loading image
        img = ImageParser.get_image(driver, self.validated_data['url'])
        if not img:
            return Response(data='Image can not be loaded', status=400)

        new_url = ImageStorage.generate_url()
        img.save(f'{MEDIA_ROOT}{new_url}')
        self.validated_data['url'] = f'{MEDIA_URL}{new_url}'

        # Calculating width, height and dominating color
        params = Photo.get_image_info(img)
        self.validated_data['width'] = params['width']
        self.validated_data['height'] = params['height']
        self.validated_data['color'] = params['color']

        self.save()
        if close_driver:
            driver.close()

        return Response(self.data, status=200)
