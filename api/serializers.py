from rest_framework import serializers
from rest_framework.response import Response
from .models import Photo

import os
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

        # Leaving url as is on update
        if self.instance is not None:
            url = self.instance.url
        # Generating new url on creation
        else:
            url = ImageStorage.generate_url()

        self.validated_data['url'] = url
        img.save(os.path.join(BASE_DIR, url))

        # Calculating width, height and dominating color
        params = Photo.get_image_info(img)
        self.validated_data['width'] = params['width']
        self.validated_data['height'] = params['height']
        self.validated_data['color'] = params['color']

        self.save()
        if close_driver:
            driver.close()

        return Response(self.data, status=200)
