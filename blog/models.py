from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, blank=True, null=True , on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stutus = models.BooleanField(default=False)
    seen_count = models.IntegerField(default=1)

    

    def __str__(self):
        return self.title



