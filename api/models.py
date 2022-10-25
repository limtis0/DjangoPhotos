from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import requests


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
    def is_url_valid(url: str):
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

