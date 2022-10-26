from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image


class Photo(models.Model):
    title = models.CharField(max_length=128)
    albumId = models.PositiveIntegerField()
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    url = models.CharField(max_length=2048)

    @classmethod
    def get_by_id(cls, pk: int):
        try:
            photo = cls.objects.get(id=pk)
        except ObjectDoesNotExist:
            photo = None
        return photo

    @staticmethod
    def _get_dominant_color(img: Image):
        img.resize((150, 150), resample=0)  # Minor optimization
        dominant_color = max(img.getcolors(maxcolors=22500), key=lambda x: x[0])  # Max count from List[(count, (RGB))]
        hex_value = '#%02x%02x%02x' % dominant_color[1]  # Filter RGB tuple to HEX string
        return hex_value

    @classmethod
    def get_image_info(cls, img: Image):
        width, height = img.size
        dominant_color = cls._get_dominant_color(img)
        return {
            'width': width,
            'height': height,
            'color': dominant_color
        }
