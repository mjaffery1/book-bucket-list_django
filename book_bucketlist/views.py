from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
# Create your views here.

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'book_bucketlist/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'book_bucketlist/author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'book_bucketlist/author_form.html', {'form': form})

def author_edit(request,pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'book_bucketlist/author_form.html', {'form': form})

def author_delete(request, pk):
    Author.objects.get(pk=pk).delete()
    return redirect('author_list')
            

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_bucketlist/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book_bucketlist/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else: 
        form = BookForm()
    return render(request, 'book_bucketlist/book_form.html', {'form': form})

def book_edit(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_bucketlist/book_form.html', {'form': form})

def book_delete(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('book_list')
            