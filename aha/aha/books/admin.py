# encoding: utf-8

from django.contrib import admin
from aha.books.models import Book, BookInfo


class BookAdmin(admin.ModelAdmin):
    pass


class BookInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(BookInfo, BookInfoAdmin)