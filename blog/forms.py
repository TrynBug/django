from django import forms
from .models import Post, PyTest

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )

class PyForm(forms.ModelForm):

    class Meta:
        model = PyTest
        fields = ('count', 'text', 'word1', 'word2', 'word3',)
