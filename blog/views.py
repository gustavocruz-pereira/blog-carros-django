from django.shortcuts import render
from blog.models import Post
from comments.models import Comentario
from produtos.models import Produtos

def home(request):
    posts = Post.objects.all().order_by('-id')
    produtos = Produtos.objects.all()
    return render(request, 'home.html', {'posts': posts, 'produtos': produtos, 'range': range(2)})

def post(request, post_id):
    posts = Post.objects.get(pk=post_id)
    comentarios = Comentario.objects.filter(post_comentario=post_id)
    return render(request, 'post.html', {'posts': posts, 'comentarios': comentarios})

def artigos(request):
    posts = Post.objects.all()
    return render(request, 'artigos.html', {'posts' : posts})

def erro404(request, exeption):
    return render(request, 'erro_404.html')
    
