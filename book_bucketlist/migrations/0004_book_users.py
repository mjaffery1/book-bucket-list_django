# Generated by Django 4.0.6 on 2022-07-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_bucketlist', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(to='book_bucketlist.user'),
        ),
    ]
