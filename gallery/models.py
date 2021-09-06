from django.db import models
from blog.models import Category

class Pictures(models.Model):
    subjecet = models.CharField(max_length=250 , blank=True,null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    images = models.ManyToManyField('Image', null=True, on_delete=models.SET_NULL)


class Image(models.Model):
    images = models.ImageField()

class Videos(models.Model):
    subjecet = models.CharField(max_length=250 , blank=True,null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    clip = models.ManyToManyField('Clips', null=True, on_delete=models.SET_NULL)

class Clips(models.Model):
    clip = models.FileField(upload_to="media/videos")  