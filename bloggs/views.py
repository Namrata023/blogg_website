from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from decouple import config
from .models import User, Category, BlogPost, Like, Comment



def index(request):
    return HttpResponse('Hello, World!')