from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArticleForm, CommentForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from decouple import config
from django.conf import settings
from .models import User, Category, Article, Like, Comment
from django.contrib.auth import authenticate, login,logout




def home(request):
    articles = Article.objects.all()
    return render(request,'home.html' , {'articles':articles})

def article_detail(request,id):
    article =Article.objects.get(id=id)
    comments = article.comments.all()
    likes_count = article.likes.count()

    if request.method == 'POST':
        if 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.article = article
                new_comment.save()
                return redirect('article_detail', id=article.id)
        elif 'like' in request.POST:
            if not Like.objects.filter(user=request.user, article=article).exists():
                Like.objects.create(user=request.user, article=article)
            return redirect('article_detail', id=article.id)
    else:
        form = CommentForm()

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
        'likes_count': likes_count
    })


    

@login_required
def create_article(request):
    if not request.user.is_author:
        return HttpResponse("You are not authorized to create an article")
    
    
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save()
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})
        
@login_required
def add_comment(request,id):
    article = Article.objects.get(id=id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', id=article.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html',{'form':form})
        

@login_required
def delete_article(request,id):
    article = Article.objects.get(id=id)
    if article.author != request.user:
        return HttpResponse('You are not authorized to delete this article')
    
    article.delete()
    return redirect('home')

@login_required
def edit_article(request,id):
    article = Article.objects.get(id=id)
    if not request.user.is_author:
        return HttpResponse('You are not authorized to edit this article')
    
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form':form})
        
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories':categories})

@login_required
def like_article(request,id):
    article = Article.objects.get(id=id)

    existing_like = Like.objects.filter(user=request.user, article=article).first()

    if existing_like:
        existing_like.delete()
    
    else:
        Like.objects.create(user=request.user, article=article)
    return redirect('article_detail', id=article.id)


def register(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid username or password')
            
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
  