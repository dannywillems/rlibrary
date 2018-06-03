from django import forms
from core.models import Book
from core.actions import build_book_object_based_on_isbn


class BookWithISBNForm(forms.ModelForm):
    use_isbn = forms.BooleanField(required=False)

    def save(self, commit=True):
        super(BookWithISBNForm, self).save(commit=commit)
        use_isbn = self.cleaned_data.get("use_isbn")
        if use_isbn is True:
            isbn = self.cleaned_data.get("isbn")
            objects = build_book_object_based_on_isbn(isbn, save=False)
            book = objects["book"]
            authors = objects["authors"]
            tags = objects["tags"]
            book.save()
            for author in authors:
                author.save()
                book.authors.add(author)
            for tag in tags:
                tag.save()
                book.tags.add(tag)
            return book
        else:
            return super(BookWithISBNForm, self).save(commit=commit)

    class Meta:
        model = Book
        fields = ("use_isbn", "isbn")


class DefaultBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("__all__")
