from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def thread(request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    comments_list = Comment.objects.filter(book=book, parent=None)

    return render(request, 'books/thread.html', {
        'book': book,
        'comments_list': comments_list,
    })

@login_required
def create_comment(request, book_id, comment_id):

    if request.method == "GET":

        book = get_object_or_404(Book, pk=book_id)

        try:
            parent_comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            parent_comment = None

        comment_form = CommentForm(
            initial={'author': request.user, 'book': book, 'parent': parent_comment})

        return render(request, 'books/create_comment.html', {
            'book': book,
            'parent_comment': parent_comment,
            'comment_form': comment_form,
        })

    else:

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save()
            new_comment.likes.add(request.user)
            return redirect(new_comment)

        return render(request, 'books/create_comment.html', {
            'book': book,
            'parent_comment': parent_comment,
            'comment_form': comment_form,
        })

def delete_comment(request, book_id, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author: return HttpResponseForbidden()

    comment.delete()
        
    return HttpResponse()

def like_comment(request, book_id, comment_id):

    if not request.user.is_authenticated: return HttpResponseForbidden()
    
    comment = get_object_or_404(Comment, pk=comment_id)

    # If the user has upvoted the comment
    if comment.likes.filter(pk=request.user.id).exists():
        comment.likes.remove(request.user)
        return HttpResponse('unlike')

    else:
        comment.likes.add(request.user)
        return HttpResponse('like')