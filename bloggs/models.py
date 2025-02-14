from django.db import models
from django.contrib.auth.models import AbstractUser
from decouple import config
from django.core.mail import send_mail

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    is_author = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='bloggs_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='bloggs_user_permissions_set', blank=True)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    

post_status_choices = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Archived', 'Archived'),
        ('Pending', 'Pending'),
]
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=100, choices=post_status_choices, default='Draft')
   
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog_post.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='author_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.username} liked {self.blog_post.title}'

