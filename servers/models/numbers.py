from django.db import models


class sthWith4(models.Model):
    icon = models.ImageField(blank=True, null=True)
    text = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.text