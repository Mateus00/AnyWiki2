from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog, Categoria
from django.utils.text import slugify

def index(request):
    return render(request, 'blog/home.html', {
        'categorias': Categoria.objects.all(),
        'posts': Blog.objects.all()
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

def novo_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        corpo = request.POST.get('corpo')
        categoria_id = request.POST.get('categoria_id')
        imagem = request.FILES.get('imagem')

        slug = slugify(titulo)
        
        # Garante que o slug seja único (pode ser melhorado com uma verificação no banco)
        count = 1
        slug_original = slug
        while Blog.objects.filter(url=slug).exists():
            slug = f"{slug_original}-{count}"
            count += 1

        Blog.objects.create(
            titulo=titulo,
            url=slug,
            corpo=corpo,
            categoria_id=categoria_id,
            imagem=imagem
        )
        return redirect('/blog/')

    categorias = Categoria.objects.all()
    return render(request, 'blog/post_form.html', {
        'categorias': categorias
    })