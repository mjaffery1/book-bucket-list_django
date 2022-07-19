# Generated by Django 4.0.6 on 2022-07-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_bucketlist', '0004_book_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.CreateModel(
            name='UserBookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(to='book_bucketlist.book')),
                ('users', models.ManyToManyField(to='book_bucketlist.user')),
            ],
        ),
    ]