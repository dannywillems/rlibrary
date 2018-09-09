from django.contrib import admin
from core import models
from core.forms import DefaultBookForm, BookWithISBNForm


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail", "publisher", "published_date")
    list_filter = ("tags", "publisher", "published_date", "authors", "language")
    search_fields = ("title", )

    def get_queryset(self, request):
        return super(BookAdmin, self).get_queryset(request).filter(user_id=request.user)

    def add_view(self, request, form_url="", extra_context=None):
        class BookWithISBNRequest(BookWithISBNForm):
            def __new__(cls, *args, **kwargs):
                kwargs["request"] = request
                return BookWithISBNForm(*args, **kwargs)
        self.form = BookWithISBNRequest

        return super(BookAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        self.form = DefaultBookForm
        return super(BookAdmin, self).change_view(request, object_id, form_url, extra_context)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", )


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Collection)
