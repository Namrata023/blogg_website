from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create_article', create_article, name='create_article'),
    path('article_detail/<int:id>', article_detail, name='article_detail'),
    path('add_comment/<int:id>', add_comment, name='add_comment'),
    path('delete_article/<int:id>', delete_article, name='delete_article'),
    path('edit_article/<int:id>', edit_article, name='edit_article'),
    path('category_list', category_list, name='category_list'),
    path('like_article/<int:id>', like_article, name='like_article'),
]
