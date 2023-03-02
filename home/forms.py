from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('full_name', 'massage')
        labels = {
            'full_name': 'Name',
            'massage': 'Message',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'massage': forms.Textarea(attrs={'class': 'form-control bg-light'})
        }
