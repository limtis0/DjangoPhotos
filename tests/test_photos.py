from api.models import Photo
from data.data_photos import DataPhotos
from PIL import Image


class TestPhotos:
    def test_get_params(self):
        img1 = Image.open('data/image_800_600_000000.png')
        info1 = Photo.get_image_info(img1)
        assert info1 == {'width': 800, 'height': 600, 'color': '#000000'}

        img2 = Image.open('data/image_500_400_22b14c.png')
        info2 = Photo.get_image_info(img2)
        assert info2 == {'width': 500, 'height': 400, 'color': '#22b14c'}
