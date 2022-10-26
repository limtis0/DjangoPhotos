import pytest
from rest_framework.test import APIClient

from api.models import Photo
from data.data_photos import DataPhotos

import os
from DjangoPhotos.settings import BASE_DIR


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="function")
def photo_applied():
    return Photo.objects.create(**DataPhotos.valid_photo)


@pytest.fixture(scope="session")
def photos_cleanup():
    def cleanup():
        for photo in Photo.objects.all():
            os.remove(os.path.join(BASE_DIR, photo.url))

    return cleanup  # Returns a callable
