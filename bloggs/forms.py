from django import forms
from .models import Article, Comment, User, Category, Like, Feedback,FAQ
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'category', 'image', 'status']
    slug = forms.SlugField(max_length=200, required=False, help_text="Leave blank to auto-generate from title.")
    
    def save(self, commit=True):
        article = super().save(commit=False)
        if not article.slug: 
            article.slug = article.title.lower().replace(" ", "-")  
        if commit:
            article.save()
        return article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your comment here...'}),        
        }   

class UserCreationForm(BaseUserCreationForm):
    is_author = forms.BooleanField(required=False, initial=False, label="Are you an author?")

    class Meta:
        model = User
        fields = ['username', 'email', 'is_author',  "password1", "password2"]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']