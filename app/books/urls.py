from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('<int:book_id>', views.thread, name='thread'),
    path('<int:book_id>/comment', views.create_comment, name='create_comment'),
]