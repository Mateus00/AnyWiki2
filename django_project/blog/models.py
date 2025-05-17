from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    url = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.titulo

    def get_url_absoluta(self):
        return reverse('ver_categoria_blog', kwargs={'slug': self.url})


class Blog(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)  # <-- agora é opcional
    corpo = models.TextField()
    data = models.DateField(db_index=True, auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    def get_url_absoluta(self):
        return reverse('ver_post_blog', kwargs={'slug': self.url})
