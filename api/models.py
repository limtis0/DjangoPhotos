from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class PhotoFields:
    id = 'id'
    title = 'title'
    albumId = 'albumId'
    url = 'url'
    width = 'width'
    height = 'height'
    dominant_color = 'color'
    file = 'file'


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
