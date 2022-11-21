from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def home(request):
    
    posts = Post.objects.all()
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

#====================================================

def about(request):
    context = {
        'title': 'من أنا',
    }
    return render(request, 'blog/about.html', context)

#=====================================================

def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'title': post.title, 
        'post' : post,
    }
    return render(request, 'blog/detail.html', context)