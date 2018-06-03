from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=256)

    def __str__(self):
        return self.full_name


class Language(models.Model):
    """
    http://www.loc.gov/standards/iso639-2/php/code_list.php
    """
    code = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.code


class Collection(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="author")
    title = models.CharField(max_length=512)
    # Create a small django plugin for that?
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=512)
    published_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="tag")
    language = models.ForeignKey(Language, to_field="code", on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    collections = models.ManyToManyField(Collection, related_name="collection")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
