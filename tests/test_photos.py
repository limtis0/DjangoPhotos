from api.models import Photo
from data.data_photos import DataPhotos


class TestPhotos:
    def test_is_url_valid(self):
        assert Photo._is_url_valid('asdfasdfasdf') is False
        assert Photo._is_url_valid('google.com') is False
        assert Photo._is_url_valid(DataPhotos.valid_photo['URL']) is True

    def test_get_image_from_url(self):
        data = Photo._get_image_info(DataPhotos.valid_photo['URL'])
        assert data['width'] == 1050 and data['height'] == 624
        assert data['color'] == '#ffffff'
