from django.db import models

# Create your models here.
class Titulo(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False)


class Categoria(models.Model):   
    nome = models.CharField(max_length=50, blank=False, null=False)


class Produto(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    preco = models.DecimalField(decimal_places=2, max_digits=6, blank=False, null=False)
    quantidade = models.PositiveIntegerField(blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=300, blank=False, null=False)


class Venda(models.Model):
    cliente = models.CharField(max_length=250, blank=False, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(null=False, blank=False)
    valor = models.DecimalField(decimal_places=2, max_digits=7, blank=False, null=False)
    
