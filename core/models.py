from django.db import models


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.URLField(unique=True)

    def __str__(self):
        return self.long_url
