from .models import Comment
from django.forms import ModelForm, CharField, Textarea, HiddenInput


class CommentForm(ModelForm):

    text = CharField(label='', widget=Textarea(attrs={
                'class': 'w-100 border-0 data-autoresize',
                'rows': 1,
                'style': 'outline: none; resize: none;',
                'placeholder': 'Write your comment here',
            }))

    class Meta:

        model = Comment
        fields = ['author', 'parent', 'book', 'text']
        widgets = {
            'author': HiddenInput(),
            'parent': HiddenInput(),
            'book': HiddenInput(),
        }
