from django.shortcuts import render
from .serializers import CategoriaSerializer, TituloSerializer, VendaSerializer, ProdutoSerializer
from .serializers import ProdutoEstoqueSerializer
from .models import Categoria, Titulo, Venda, Produto
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import UserPermissions
# Create your views here.


# Criando a View de Categoria, para adicionar e listar
# POST e GET Categoria
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Criando a View do Título para adicionar e listar
# POST e GET Título
class TituloListCreateView(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Criando a View do Produto para adicionar e listar
# POST e GET
class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Criando a View do Produto para atualizar, detalhar e deletar com o ID
# GET, UPDATE e DELETE
class ProdutoDetailDeleteUpView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Criando uma View de Produto para atualizar o estoque - Venda ou Reposição
class ProdutoUpdateEstoqueView(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoEstoqueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
# Criando uma View de Produto para listar e criar vendas
class VendasListCreateView(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        venda = self.get_object()
        return Response(venda)

    def post(self, request, pk=None):
        venda = self.get_object()
        produtos_data = venda.produtos

        for produto_id, quantidade in produtos_data.items():
            try:
                produto = Produto.objects.get(id=produto_id)
                if produto.quantidade < quantidade:
                    return Response({"error": f"Estoque insuficiente para {produto_id}"})
                
                # Aqui reduziremos o estoque
                produto.quantidade -= quantidade
                produto.save()
            except Produto.DoesNotExist:
                return Response({"error": f"Produto ID {produto_id} não encontrado!"})

        return Response({"message": "Venda processada!"}, status=status.HTTP_201_CREATED)

