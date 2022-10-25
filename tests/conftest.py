import pytest
from rest_framework.test import APIClient

from api.models import Photo
from data.data_photos import DataPhotos


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="function")
def photo_applied():
    return Photo.objects.create(**DataPhotos.valid_photo)
