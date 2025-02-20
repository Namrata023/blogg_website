from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArticleForm, CommentForm, UserCreationForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from decouple import config
from django.conf import settings
from .models import User, Category, Article, Like, Comment,Feedback,FAQ
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseForbidden



def home(request):
    articles = Article.objects.all()
    return render(request,'base.html' , {'articles':articles})


def blog(request):
    articles = Article.objects.all()  
    return render(request, 'blog.html', {'articles': articles})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')


def cookies(request):
    return render(request, 'cookies.html')



def article_detail(request, id, slug):
    article = Article.objects.get(id=id, slug=slug)
        
    
    comments = article.comments.all()
    likes_count = article.likes.count()
    form = CommentForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.article = article
                new_comment.save()
                return redirect('article_detail', id=article.id, slug=article.slug)
        elif 'like' in request.POST:
            if Like.objects.filter(user=request.user, article=article).exists():
               
                Like.objects.filter(user=request.user, article=article).delete()
            else:
                
                Like.objects.create(user=request.user, article=article)
            return redirect('article_detail', id=article.id, slug=article.slug)
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
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})
        

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)

    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    article = comment.article
    comment.delete()

    return redirect('article_detail', id=article.id, slug=article.slug) 

@login_required
def delete_article(request,slug):
    article = Article.objects.get(slug=slug)
    if not request.user.is_author:
        return HttpResponse('You are not authorized to delete this article')
    
    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            article.delete()
            return redirect('home')  # Redirect to homepage after deletion
        elif 'cancel_delete' in request.POST:
            return redirect('article_detail', id=article.id, slug=slug)  # Redirect back to the article detail page

    return render(request, 'delete_article.html', {'article': article})



@login_required
def edit_article(request,slug):
    article = Article.objects.get(slug=slug)
    if not request.user.is_author:
        return HttpResponse('You are not authorized to edit this article')
    
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail',id=article.id, slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form':form})


        
def category_list(request):
    category = Category.objects.all()

    return render(request, 'category_list.html', {'category':category})




def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            login(request, user)

            subject = "Welcome to Blogger's Haven"
            message = "Thank you for registering! We are glad to have you."
            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email]

            send_mail(subject, message, from_email, to_email)
            return redirect('login_view')
    
        # form = UserCreationForm()
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
            return render(request, 'login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})

@login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')  
    
        form = FeedbackForm()
    
    return render(request, 'feedback_create.html', {'form': form})



def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    return render(request, 'search_results.html', {'articles': articles})