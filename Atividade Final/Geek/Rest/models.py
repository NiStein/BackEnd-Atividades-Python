from django.db import models

# Create your models here.
class Titulo(models.Model):
    nome = models.CharField(max_length=60, blank=False, null=False)
    descricao = models.CharField(max_length=600, blank=False, null=False)

    def __str__(self):
        return f'{self.nome}'


class Categoria(models.Model):   
    nome = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return f'{self.nome}'


class Produto(models.Model):
    nome = models.CharField(max_length=60, blank=False, null=False)
    preco = models.DecimalField(decimal_places=2, max_digits=6, blank=False, null=False)
    quantidade = models.PositiveIntegerField(blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=300, blank=False, null=False)
    def __str__(self):
        return f'{self.nome} {self.preco} {self.quantidade}'


class Venda(models.Model):
    cliente = models.CharField(max_length=300, blank=False, null=False)
    data_hora = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    produtos = models.JSONField(default=dict)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.cliente} {self.valor_total}'
