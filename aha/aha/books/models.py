# encoding: utf-8

from django.db import models
from aha.readers.models import Reader

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
    image_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class BookInfo(models.Model):

    READ_STATUS_CHOICE = (
        (1, '想读'),
        (2, '在读'),
        (3, '读过'),
    )

    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024)
    read_status = models.SmallIntegerField(choices=READ_STATUS_CHOICE)

    def __str__(self):
        return '<<%s>>的信息' % self.book.title

