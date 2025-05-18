# loja/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Auto-popula slug ao salvar se não estiver preenchido
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('loja:produtos_por_categoria', args=[self.slug])


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    data_adicionado = models.DateTimeField(auto_now_add=True)
    promocao = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('loja:produto_detalhes', args=[self.pk])


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40)  # vincula ao visitante

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
