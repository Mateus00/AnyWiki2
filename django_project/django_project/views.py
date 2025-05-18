from django.shortcuts import render
from blog.models import Blog
from loja.models import Produto  # Certifique-se de importar corretamente o model Produto

def homepage(request):
    # Últimos 5 posts do blog
    posts = Blog.objects.order_by('-data')[:5]

    # Últimos 10 produtos adicionados
    produtos_destaque = Produto.objects.order_by('-data_adicionado')[:10]

    # Até 10 produtos com promoção ativa
    ofertas = Produto.objects.filter(promocao=True).order_by('-data_adicionado')[:10]

    context = {
        'ultimos_posts': posts,
        'produtos_destaque': produtos_destaque,
        'ofertas': ofertas,
    }

    return render(request, 'home.html', context)

def posts(request):
    return render(request, 'posts.html')

def sobre(request):
    return render(request, 'about.html')
