from django.contrib import admin
from blog.models import Blog, Categoria

class BlogAdmin(admin.ModelAdmin):
    exclude = ['data']
    prepopulated_fields = {'url': ('titulo',)}  # corrigido de 'slug' para 'url'

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('titulo',)}  # corrigido de 'slug' para 'url'

admin.site.register(Blog, BlogAdmin)
admin.site.register(Categoria, CategoriaAdmin)