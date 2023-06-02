from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural= 'Categorias'

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    categoria          = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE) # se deletar a categoria, todos os produtos ligados a categoria serão deletados
    cadastrado_por     = models.ForeignKey(User, related_name='produtos', on_delete=models.CASCADE) # se deletar o User, todos os produtos ligados ao User serão deletados
    nome               = models.CharField(max_length=255)    
    marca              = models.CharField(max_length=255, blank=True, null=True)
    modelo             = models.CharField(max_length=255, blank=True, null=True)
    tamanho            = models.CharField(max_length=255, blank=True, null=True)
    unid_por_embalagem = models.CharField(max_length=255, blank=True, null=True)
    descrição          = models.TextField(blank=True, null=True)
    preço              = models.FloatField()
    imagem             = models.ImageField(upload_to="produto_imagens", blank=True, null=True)
    em_estoque         = models.BooleanField(default=False)
    data_criação       = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)        

    def __str__(self):
        return self.nome
