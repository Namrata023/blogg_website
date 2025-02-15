from django import forms
from .models import Article, Comment, User, Category, Like, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        