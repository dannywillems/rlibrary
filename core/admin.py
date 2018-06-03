from django.contrib import admin
from core import models
from core.forms import DefaultBookForm, BookWithISBNForm


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail", "publisher", "published_date")
    list_filter = ("tags", "publisher", "published_date", "authors", "language")
    search_fields = ("title", )

    def add_view(self, request, form_url="", extra_context=None):
        class Form(BookWithISBNForm):
            def __new__(cls, *args, **kwargs):
                kwargs["request"] = request
                return BookWithISBNForm(*args, **kwargs)
        self.form = Form
        return super(BookAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        class Form(DefaultBookForm):
            def __new__(cls, *args, **kwargs):
                kwargs["request"] = request
                return DefaultBookForm(*args, **kwargs)
        self.form = Form
        return super(BookAdmin, self).change_view(request, object_id, form_url, extra_context)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", )


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Collection)
