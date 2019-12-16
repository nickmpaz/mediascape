from django.shortcuts import render
from books.models import Book


def index(request):

    books_list = sorted(
        Book.objects.all(), key=lambda book: book.comment_set.count(), reverse=True)

    return render(request, 'home/index.html', {
        'books_list': books_list
    })
