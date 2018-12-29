from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from aha.readers.models import Reader


class ReaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reader, ReaderAdmin)
