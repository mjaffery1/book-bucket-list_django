from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()


    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE, related_name='books')
    title= models.CharField(max_length=120, default= 'no book title')
    description= models.TextField()
    year= models.IntegerField()
    cover_url= models.TextField()
    users = models.ManyToManyField(User, through='UserBookList')
    

    def __str__(self):
        return self.title

class UserBookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
