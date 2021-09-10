from django.db import models
from categories.models import Category

class Pictures(models.Model):
    subjecet = models.CharField(max_length=250 , blank=True,null=True, verbose_name='موضوع عکس')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='دسته بندی عکس')
    images = models.ManyToManyField('Image', verbose_name='عکس ها')


class Image(models.Model):
    images = models.ImageField(verbose_name='عکس')

class Videos(models.Model):
    subjecet = models.CharField(max_length=250 , blank=True,null=True, verbose_name='موضوع فیلم')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='دسته بندی فیلم')
    clip = models.ManyToManyField('Clips', verbose_name='فیلم')

class Clips(models.Model):
    clip = models.FileField(upload_to="media/videos", verbose_name='فیلم')  