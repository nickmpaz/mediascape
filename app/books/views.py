from django.shortcuts import render, get_object_or_404
from .models import Book, Comment

def thread(request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    comments_list = Comment.objects.filter(book=book, parent=None)
    
    return render(request, 'books/thread.html', {
        'book': book,
        'comments_list': comments_list,
    })

def create_comment(request, book_id):

    if request.method == "GET":

        book = Book.objects.get(pk=book_id)

        return render(request, 'books/create_comment.html', {
            'book': book,
            'comments_list': None,
        })

    else:

        pass