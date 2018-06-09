# Generated by Django 2.0 on 2018-06-09 21:49

from django.db import migrations, models
from core.models import BookType

import django.db.models.deletion


def add_predefined_book_type(apps, schema_editor):
    BookType.objects.bulk_create([
        BookType(name="Hardcover"),
        BookType(name="Softcover"),
        BookType(name="EPUB")
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_book_bought_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.BookType'),
        ),
        migrations.RunPython(add_predefined_book_type)
    ]
