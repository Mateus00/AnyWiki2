# loja/urls.py
from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:pk>/', views.produto_detalhes, name='produto_detalhes'),
    path('categoria/<slug:slug>/', views.produtos_por_categoria, name='produtos_por_categoria'),    
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
