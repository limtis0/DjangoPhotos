from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=128)
    albumID = models.PositiveIntegerField()
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    URL = models.CharField(max_length=2048)

    # String representation for debugging
    def __str__(self):
        return self.title
