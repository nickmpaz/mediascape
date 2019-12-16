from .models import Comment
from django.forms import ModelForm, Textarea

class CommentForm(ModelForm):

    class Meta:
    
        model = Comment
        fields = ['parent', 'book', 'text']
        widgets = {
            'text': Textarea(attrs={
                'class': 'w-100 border-0 data-autoresize',
                'rows': 1,
                'style': 'outline: none; resize: none;',
                'placeholder': 'Write your comment here',
            }),
        }