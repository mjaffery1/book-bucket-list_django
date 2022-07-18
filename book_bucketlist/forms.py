from django import forms
from .models import Author, Book, User

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'photo_url',)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name',)

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'cover_url', 'year', 'description', 'author',)