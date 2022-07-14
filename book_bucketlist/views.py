from django.shortcuts import render
from .models import Author, Book
# Create your views here.

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'book_bucketlist/author_list', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_bucketlist/book_list', {'books': books})