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
        fields = ['cliente', 'data_hora', 'produtos', 'valor_total']

    def create(self, validated_data):
        produtos_data = validated_data.pop('produtos') # Armazena os produtos na variavel
        venda = Venda.objects.create(**validated_data) # Cria a venda sem os produtos, pois estes serão tratados

        # Agora iremos validar os ID dos produtos, se eles existem no banco de dados
        valor_total = 0
        for produto_id, quantidade in produtos_data.items():
            try:
                produto = Produto.objects.get(id=produto_id)
                valor_total += produto.preco * quantidade
            except Produto.DoesNotExist:
                raise serializers.ValidationError({"error": f"Produto ID {produto_id} não encontrado!"})
            
        venda.produtos = produtos_data
        venda.valor_total = valor_total
        venda.save()

        return venda


