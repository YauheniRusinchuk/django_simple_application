from django import forms
from core.models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(label="",
        widget = forms.TextInput(attrs={
            'placeholder': 'Title...',
            'class': 'addpost_title'
        })
    )


    body = forms.CharField(label="",
        widget = forms.Textarea(attrs={
            'class': 'addpost_content',
            'placeholder': 'Content...'
        })
    )


    class Meta:
        model = Post
        fields = ('title', 'body', 'img')
