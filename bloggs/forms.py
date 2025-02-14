from django import forms
from .models import BlogPost, Comment, User, Category, Like, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        