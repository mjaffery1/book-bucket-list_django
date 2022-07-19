from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name= 'author_list'),
    path('authors/', views.author_list, name= 'author_list'),
    path('authors/<int:pk>', views.author_detail, name='author_detail'),
    path('authors/new', views.author_create, name='author_create'),
    path('authors/<int:pk>/edit', views.author_edit, name='author_edit'),
    path('authors/<int:pk>/delete', views.author_delete, name='author_delete'),
    path('books/', views.book_list, name= 'book_list'),
    path('books/<int:pk>', views.book_detail, name= 'book_detail'),
    path('books/new', views.book_create, name='book_create'),
    path('books/<int:pk>/edit', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('users/', views.user_list, name= 'user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
    path('books/<int:pk>/add', views.add_book_to_user, name = 'add_book_to_user')
    ]
