from django.shortcuts import render
from .serializers import CategoriaSerializer, TituloSerializer, VendaSerializer, ProdutoSerializer
from .serializers import ProdutoEstoqueSerializer
from .models import Categoria, Titulo, Venda, Produto
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


# Criando a View de Categoria, para adicionar e listar
# POST e GET Categoria
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# Criando a View do Título para adicionar e listar
# POST e GET Título
class TituloListCreateView(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer

# Criando a View do Produto para adicionar e listar
# POST e GET
class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# Criando a View do Produto para atualizar, detalhar e deletar com o ID
# GET, UPDATE e DELETE
class ProdutoDetailDeleteUpView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# Criando uma View de Produto para atualizar o estoque - Venda ou Reposição
class ProdutoUpdateEstoqueView(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoEstoqueSerializer
    
# Criando uma View de Produto para listar e criar vendas
class VendasListCreateView(APIView):
    
    def get(self, request):
        vendas = Venda.objects.all()
        serializer = VendaSerializer(vendas, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

