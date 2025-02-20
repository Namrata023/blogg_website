from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
    path('create_article', create_article, name='create_article'),
    path('article_detail/<int:id>/<slug:slug>/', article_detail, name='article_detail'),
   
    path('delete_article/<slug:slug>/', delete_article, name='delete_article'),
    path('edit_article/<slug:slug>/', edit_article, name='edit_article'),
    path('category_list/', category_list, name='category_list'),
    
    path('login_view', login_view, name='login_view'),
    path('logout_view', logout_view, name='logout_view'),
    path('register', register, name='register'),
    path('faq_list/', faq_list, name='faq_list'),
    path('feedback_create/', feedback_create, name='feedback_create'),
    path('search/', search, name='search'),
    path('privacy/', privacy, name='privacy'),
    path('cookies/', cookies, name='cookies'),
    path('delete_comment/<int:id>/', delete_comment, name='delete_comment'),


]
