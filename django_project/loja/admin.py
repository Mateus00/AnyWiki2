# loja/admin.py
from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'promocao', 'data_adicionado')
    search_fields = ('nome',)
    list_filter = ('categoria', 'promocao', 'data_adicionado')
    list_editable = ('promocao',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
