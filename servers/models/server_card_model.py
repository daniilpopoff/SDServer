from django.db import models

class ServerCardModel(models.Model):
    name = models.CharField(max_length=200)
    price =  models.CharField()
    photo = models.ImageField(upload_to=pics)
    make_by = models.CharField(help_text='Производитель')
    description =  models.TextField()
    slug = models.SlugField(unique=True)
    characteristics = models.TextField()
    
