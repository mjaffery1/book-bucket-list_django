from django.shortcuts import render, redirect
from .models import Author, Book, User, UserBookList
from .forms import AuthorForm, BookForm, UserForm, UserBookForm
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
            
def user_list(request):
    users = User.objects.all()
    return render(request, 'book_bucketlist/user_list.html', {'users': users})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    list = UserBookList.objects.filter(user_id=user.id)
    print(list)
    return render(request, 'book_bucketlist/user_detail.html', {'user': user, 'list': list})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'book_bucketlist/user_form.html', {'form': form})

def user_edit(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'book_bucketlist/user_form.html', {'form': form})

def user_delete(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('user_list')

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

def add_book_to_user(request, pk):
    list = UserBookList()
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        # Gets user id from form data when submitting
        user = User.objects.get(id=request.POST["users"])
        form = UserBookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            # list.save()
            list.user = user
            list.book = book
            print(list.user)
            print(list.book)
            # list.save()

            # print(book)
            return redirect('book_detail', pk=book.pk)
    else:
        # users = User.objects.all() 
        form = UserBookForm()
        return render(request, 'book_bucketlist/add_book.html', {'form': form})

            