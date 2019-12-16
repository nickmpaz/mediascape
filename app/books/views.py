from django.shortcuts import render, get_object_or_404
from .models import Book, Comment
from .forms import CommentForm


def thread(request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    comments_list = Comment.objects.filter(book=book, parent=None)
    
    return render(request, 'books/thread.html', {
        'book': book,
        'comments_list': comments_list,
    })

def create_comment(request, book_id):

    if request.method == "GET":

        book = get_object_or_404(Book, pk=book_id)
        comment_form = CommentForm(initial={'book': book})

        try:
            parent_comment = Comment.objects.get(pk=request.GET.get("parent"))
        except Comment.DoesNotExist:
            parent_comment = None

        return render(request, 'books/create_comment.html', {
            'book': book,
            'parent_comment': parent_comment,
            'comment_form': comment_form,
        })

    else:

        pass