from django.db import models
from categories.models import Category
from django.utils.html import format_html

class Pictures(models.Model):
    subject = models.CharField(max_length=250 , blank=True,null=True, verbose_name='موضوع عکس')
    slug = models.SlugField(max_length=100, unique=True,verbose_name="اسلاگ عکس")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='دسته بندی عکس')
    images = models.ManyToManyField('Image', verbose_name='عکس ها')
    thumbnail = models.ImageField(null=True,blank=True,upload_to="images/article",verbose_name='عکس بند انگشتی')

    def thumbnail_tag(self):
        if self.thumbnail:
            return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))

    class Meta:
        verbose_name = 'گالری عکس '
        verbose_name_plural = 'گالری عکس ها '

    def __str__(self):
        return self.subject


class Image(models.Model):
    images = models.ImageField(verbose_name='عکس')

class Videos(models.Model):
    subject = models.CharField(max_length=250 , blank=True,null=True, verbose_name='موضوع فیلم')
    slug = models.SlugField(max_length=100, unique=True,verbose_name="اسلاگ فیلم")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='دسته بندی فیلم')
    clip = models.ManyToManyField('Clips', verbose_name='فیلم')
    thumbnail = models.ImageField(default='test.png',null=True,blank=True,upload_to="images/article",verbose_name='عکس بند انگشتی')

    def thumbnail_tag(self):
        if self.thumbnail:
            return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))

    class Meta:
        verbose_name = 'گالری فیلم '
        verbose_name_plural = 'گالری فیلم ها '


    def __str__(self):
        return self.subject

class Clips(models.Model):
    clip = models.FileField(upload_to="media/videos", verbose_name='فیلم')  