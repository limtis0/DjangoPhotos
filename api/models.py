from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError

import requests
from PIL import Image
from io import BytesIO


class Photo(models.Model):
    title = models.CharField(max_length=128)
    albumID = models.PositiveIntegerField()
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    URL = models.CharField(max_length=2048)

    @classmethod
    def get_by_id(cls, pk: int):
        try:
            photo = cls.objects.get(id=pk)
        except ObjectDoesNotExist:
            photo = None
        return photo

    @staticmethod
    def _is_url_valid(url: str):
        try:
            # Validate URL structure
            URLValidator()(url)

            # Assert it leads to an image
            image_formats = ("image/png", "image/jpeg", "image/jpg")
            r = requests.head(url)
            if r.headers["content-type"] in image_formats:
                return True
        except ValidationError:
            pass
        return False

    @staticmethod
    def _get_image_from_url(url: str) -> Image:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    @staticmethod
    def _get_dominant_color(img: Image):
        img.resize((150, 150), resample=0)  # Minor optimization
        dominant_color = max(img.getcolors(maxcolors=22500), key=lambda x: x[0])  # Max count from List[(count, (RGB))]
        hex_value = '#%02x%02x%02x' % dominant_color[1]  # Filter RGB tuple to HEX string
        return hex_value

    @classmethod
    def get_image_info(cls, url: str):
        if not cls._is_url_valid(url):
            return {}

        img = cls._get_image_from_url(url)
        width, height = img.size
        dominant_color = cls._get_dominant_color(img)

        return {
            'width': width,
            'height': height,
            'color': dominant_color
        }
