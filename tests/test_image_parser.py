from data_import.image_parser import ImageParser
from data.data_photos import DataPhotos


class TestParsers:
    def test_get_image_requests(self):
        assert ImageParser._get_image_requests(DataPhotos.valid_photo['URL']) is not False
        assert ImageParser._get_image_requests(DataPhotos.valid_photo_2['URL']) is False  # Blocked by CloudFlare

    def test_get_image_selenium(self):
        assert ImageParser._get_image_selenium(DataPhotos.invalid_photo['URL']) is False
        assert ImageParser._get_image_selenium(DataPhotos.valid_photo_2['URL']) is not False
