from django.db import models
from django.contrib.auth.models import AbstractUser
from decouple import config
from django.core.mail import send_mail
from django.utils.text import slugify

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    is_author = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
   
    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

post_status_choices = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
]
class Article(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=100, choices=post_status_choices, default='Draft')
    
   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        is_new = self.id is None   
        super().save(*args, **kwargs)


        if self.status == 'Published' and not self.id:
            send_mail(
                f"New Article Published: {self.title}",
                f"A new article titled '{self.title}' has been published. Check it out!",
                config('EMAIL_HOST_USER'),
                [self.author.email],  
                fail_silently=False,
            )


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.article.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.username} liked {self.article.title}'

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Feedback from {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_mail(
            f'Feedback from {self.user.username} on {self.subject}',
            f'{self.message}',
            config('EMAIL_HOST_USER'),
            [config('EMAIL_HOST_USER')],
            fail_silently=False,
        )