from rest_framework import serializers
from Rest.models import Categoria, Titulo, Produto, Venda


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['quantidade']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

