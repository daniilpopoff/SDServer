from django.db import models


class Carusel(models.Model):
    upper_text = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    link = models.URLField(null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.text