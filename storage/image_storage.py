import shortuuid
from PIL import Image

from pathlib import Path
from DjangoPhotos.settings import BASE_DIR, MEDIA_URL


class ImageStorage:
    @staticmethod
    def generate_url(albumId) -> Path:
        return Path(MEDIA_URL, str(albumId), f'{shortuuid.uuid()}.png')

    @staticmethod
    def save_image(img: Image, path: Path):
        parent = path.parent
        if not parent.exists():
            parent.mkdir()
        img.save(path)

    @staticmethod
    def remove(url: str):
        Path(BASE_DIR, url).unlink(missing_ok=True)
