from django import forms
from .models import Article, Comment, User, Category, Like, Comment
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']    

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_author']
