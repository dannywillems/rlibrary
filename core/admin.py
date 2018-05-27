from django.contrib import admin
from core import models


class BookAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "editor")
    list_filter = ("tags", )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag)
