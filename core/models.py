from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    # Create a small django plugin for that?
    isbn = models.CharField(max_length=13)
    editor = models.CharField(max_length=512)
    tags = models.ManyToManyField(Tag, related_name="tag")
