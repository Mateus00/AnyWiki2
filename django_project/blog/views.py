from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Categoria

def index(request):
    return render(request, 'blog/home.html', {
        'categorias': Categoria.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def ver_post(request, slug):
    return render(request, 'blog/ver_post.html', {
        'post': get_object_or_404(Blog, url=slug)
    })

def ver_categoria(request, slug):
    categoria = get_object_or_404(Categoria, url=slug)
    return render(request, 'blog/ver_categoria.html', {
        'categoria': categoria,
        'posts': Blog.objects.filter(categoria=categoria)[:5]
    })