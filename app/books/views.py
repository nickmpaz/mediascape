from django.shortcuts import render, get_object_or_404
from .models import Book, Comment

def thread(request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    comments_list = Comment.objects.filter(book=book, parent=None)
    
    return render(request, 'books/thread.html', {
        'book': book,
        'comments_list': comments_list,
    })
