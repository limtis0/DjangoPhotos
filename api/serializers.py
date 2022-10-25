from rest_framework import serializers
from rest_framework.response import Response
from .models import Photo


class OutputPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class InputPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'albumID', 'URL')

    def save_photo(self):
        if not self.is_valid():
            return Response(status=400)
        self.save()
        return Response(self.data, status=200)
