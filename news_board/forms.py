from django import forms

from news_board.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'title_tag',
                  'body',
                  'link',
                  'author',
                  )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'id', 'type': 'hidden'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'body',
                  'link',
                  )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'body']

        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'id', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
