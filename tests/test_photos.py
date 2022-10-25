from api.models import Photo
from data.data_photos import DataPhotos


class TestPhotos:
    def test_url_check(self):
        assert Photo.is_url_valid('asdfasdfasdf') is False
        assert Photo.is_url_valid('google.com') is False
        assert Photo.is_url_valid(DataPhotos.valid_photo['URL']) is True
