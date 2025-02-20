from django.contrib import admin
from .models import User, Category, Article, Like, Comment,FAQ, Feedback

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(FAQ)
admin.site.register(Feedback)

