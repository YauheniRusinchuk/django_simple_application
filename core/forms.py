from django import forms
from core.models import Comment

class CommentForm(forms.ModelForm):

    text = forms.CharField(label="",
        widget = forms.TextInput(attrs={
            'placeholder': 'comment ...',
            'class': 'text_comment'
        })
    )

    class Meta:
        model = Comment
        fields = ('text',)
