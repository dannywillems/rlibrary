# Generated by Django 2.0.5 on 2018-05-28 22:13

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='editor',
            new_name='publisher',
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='full_name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='author', to='core.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(default='en', on_delete=django.db.models.deletion.CASCADE, to='core.Language'),
            preserve_default=False,
        ),
    ]
