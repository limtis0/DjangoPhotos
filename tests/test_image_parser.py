from data_import.image_parser import ImageParser
from data.data_photos import DataPhotos


class TestParsers:
    def test_get_image_requests(self):
        assert ImageParser._get_image_requests(DataPhotos.valid_photo['url']) is not False
        assert ImageParser._get_image_requests(DataPhotos.valid_photo_2['url']) is False  # Blocked by CloudFlare

    def test_get_image_selenium(self):
        assert ImageParser._get_image_selenium(DataPhotos.invalid_photo['url']) is False
        assert ImageParser._get_image_selenium(DataPhotos.valid_photo_2['url']) is not False
