from django.db import models


class Discount(models.Model):
    title = models.CharField(max_length=255)
    image_icon = models.ImageField(blank=True, null=True)
    link = models.URLField( blank=True , max_length=200)

    def __str__(self):
        return self.title
    
class One_discount(models.Model):
    text = models.CharField(max_length=225)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return self.text