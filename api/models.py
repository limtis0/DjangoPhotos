from django.db import models
from django.core.exceptions import ObjectDoesNotExist


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
