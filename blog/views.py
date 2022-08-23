from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, post_id):
    post = Post.obj.get(pk=post_id)
    return render(request, 'post.html', {'posts': post})
