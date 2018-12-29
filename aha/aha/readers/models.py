# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Reader(models.Model):
    reader = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, default='12312341234')
    # TODO: 读者特定信息字段


    def __str__(self):
        return self.reader.username
