from datetime import datetime

from django.conf import settings
from django.db import models


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_pic/', default=None, blank=True, null=True)


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField(max_length=1000)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
