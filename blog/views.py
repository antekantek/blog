from django.shortcuts import render
from .models import Post
from django.utils import timezone



# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})