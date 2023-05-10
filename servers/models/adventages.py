from django.db import models


class Adventage(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image_icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title