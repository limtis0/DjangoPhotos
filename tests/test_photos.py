from api.models import Photo


class TestPhotos:
    def test_url_check(self):
        assert Photo.is_url_valid('asdfasdfasdf') is False
        assert Photo.is_url_valid('google.com') is False
        assert Photo.is_url_valid('https://via.placeholder.com/600/92c952') is True
