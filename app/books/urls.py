from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('<int:book_id>', views.thread, name='thread'),
    path('<int:book_id>/comment/<int:comment_id>', views.create_comment, name='create_comment'),
    path('<int:book_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete-comment'),
    path('<int:book_id>/comment/<int:comment_id>/like', views.like_comment, name='like-comment'),
]