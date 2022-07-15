from django.shortcuts import render
from .models import Author, Book
# Create your views here.

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'book_bucketlist/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, 'book_bucketlist/author_detail.html', {'author': author})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_bucketlist/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book_bucketlist/book_detail.html', {'book': book})

