from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post     #声明使用models.Post
        fields = [
            'title',
            'content'
        ]