import pytest
from rest_framework.test import APIClient
from data_import.webdriver import WebDriver

from api.models import Photo
from testdata.data_photos import DataPhotos
from api.serializers import InputPhotoSerializer

from pathlib import Path
from DjangoPhotos.settings import BASE_DIR


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session")
def api_client():
    yield APIClient()

    # After-session cleanup
    WebDriver.close()


@pytest.fixture(scope="function")
def photo_applied():
    serializer = InputPhotoSerializer(data=DataPhotos.valid_photo)
    serializer.save_photo()
    return Photo.get_by_id(1)


@pytest.fixture()
def photo_cleanup():
    yield None
    for photo in Photo.objects.all():
        Path(BASE_DIR, photo.url).unlink()
