from django.shortcuts import render
from .models import Post
from django.utils import timezone




def list(request):
    posts = Post.objects.all()
    return render(request, 'blogpost.html', {'posts': posts})