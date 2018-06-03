import rlibrary.settings
import dateparser

from core.models import Author, Book, Tag, Language


def build_book_object_based_on_isbn(isbn, save=False):
    response = rlibrary.settings.GOOGLE_BOOK_API.list(isbn)
    item = response["items"][0]
    volume_info = item["volumeInfo"]
    if "subtitle" in volume_info:
        title = "{} - {}".format(volume_info["title"], volume_info["subtitle"])
    else:
        title = "{}".format(volume_info["title"])
    publisher = volume_info.get("publisher", "")
    published_date = dateparser.parse(volume_info["publishedDate"])
    language = volume_info["language"]
    categories = volume_info.get("categories", [])
    authors = volume_info["authors"]
    isbn = isbn
    if "imageLinks" in volume_info:
        thumbnail = volume_info["imageLinks"].get("smallThumbnail", "")
    else:
        thumbnail = ""
    authors_obj = []
    tags = []
    for author in authors:
        author_obj = Author.objects.get_or_create(full_name=author)[0]
        authors_obj.append(author_obj)
    for category in categories:
        tag = Tag.objects.get_or_create(name=category)[0]
        tags.append(tag)
    language = Language.objects.get_or_create(code=language)[0]
    data = {
        # "authors": authors_obj,
        "title": title,
        "isbn": isbn,
        "publisher": publisher,
        "published_date": published_date,
        # "tags": tags,
        "language": language,
        "thumbnail": thumbnail,
    }
    book = Book(**data)
    if save is True:
        for author in authors_obj:
            author.save()
            book.authors.add(author)
        for tag in tags:
            tag.save()
            book.tags.add(tag)
        book.save()
    return {"book": book, "authors": authors_obj, "tags": tags}
