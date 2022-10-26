from api.models import Photo
from data.data_photos import DataPhotos


class TestPhotos:
    def test_get_image_from_url(self):
        info = Photo.get_image_info(DataPhotos.valid_photo['URL'])
        assert info == DataPhotos.valid_photo_info
