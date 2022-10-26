import os
import shortuuid
from PIL import Image
from DjangoPhotos.settings import BASE_DIR, MEDIA_URL


class ImageStorage:
    @staticmethod
    def generate_url(albumId):
        return os.path.join(MEDIA_URL, str(albumId), f'{shortuuid.uuid()}.png')

    @staticmethod
    def save_image(img: Image, path: str):
        parent = os.path.dirname(path)
        if not os.path.exists(parent):
            os.mkdir(parent)
        img.save(path)

    @staticmethod
    def remove(url: str):
        os.remove(os.path.join(BASE_DIR, url))
