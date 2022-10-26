import os
import shortuuid
from DjangoPhotos.settings import MEDIA_URL


class ImageStorage:
    @staticmethod
    def generate_url():
        return os.path.join(MEDIA_URL, f'{shortuuid.uuid()}.png')
