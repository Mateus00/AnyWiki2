# loja/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, ItemCarrinho, Categoria

def get_carrinho(request):
    if not request.session.session_key:
        request.session.save()
    return ItemCarrinho.objects.filter(session_key=request.session.session_key)

def index(request):
    produtos = Produto.objects.all()
    carrinho = get_carrinho(request)
    return render(request, 'loja/index.html', {'produtos': produtos, 'carrinho': carrinho})

def produto_detalhes(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    relacionados = Produto.objects.filter(categoria=produto.categoria).exclude(pk=produto.pk)[:6]
    carrinho = get_carrinho(request)
    return render(request, 'loja/produto_detalhes.html', {
        'produto': produto,
        'relacionados': relacionados,
        'carrinho': carrinho
    })

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if not request.session.session_key:
        request.session.save()
    item, criado = ItemCarrinho.objects.get_or_create(produto=produto, session_key=request.session.session_key)
    if not criado:
        item.quantidade += 1
        item.save()
    return redirect(request.META.get('HTTP_REFERER', 'loja:index'))

def remover_do_carrinho(request, item_id):
    if not request.session.session_key:
        request.session.save()
    item = get_object_or_404(ItemCarrinho, id=item_id, session_key=request.session.session_key)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'loja:index'))

def produtos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    produtos = Produto.objects.filter(categoria=categoria)
    carrinho = get_carrinho(request)
    return render(request, 'loja/produtos_por_categoria.html', {
        'categoria': categoria,
        'produtos': produtos,
        'carrinho': carrinho
    })

def ver_carrinho(request):
    carrinho = get_carrinho(request)
    return render(request, 'loja/carrinho.html', {'carrinho': carrinho})
