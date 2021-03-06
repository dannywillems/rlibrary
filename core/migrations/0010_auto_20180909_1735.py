# Generated by Django 2.0 on 2018-09-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_book_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='collections',
            field=models.ManyToManyField(related_name='collection', to='core.Collection'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='tag', to='core.Tag'),
        ),
    ]
