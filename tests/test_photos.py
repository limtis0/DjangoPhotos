from PIL import Image
from data_import.image_parser import ImageParser
from testdata.data_photos import DataPhotos


class TestPhotos:
    def test_get_params(self):
        img1 = Image.open(DataPhotos.test_image_1)
        info1 = ImageParser.get_image_info(img1)
        assert info1 == DataPhotos.test_image_1_info

        img2 = Image.open(DataPhotos.test_image_2)
        info2 = ImageParser.get_image_info(img2)
        assert info2 == DataPhotos.test_image_2_info
