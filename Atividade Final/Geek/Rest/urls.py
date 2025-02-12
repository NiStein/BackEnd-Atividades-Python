from django.urls import path, include
from Rest.views import CategoriaListCreateView, TituloListCreateView, ProdutoListCreateView
from Rest.views import ProdutoUpdateEstoqueView, ProdutoDetailDeleteUpView, VendasListCreateView

urlpatterns = [
    path('categoria', CategoriaListCreateView.as_view()),
    path('titulo', TituloListCreateView.as_view()),
    path('produto', ProdutoListCreateView.as_view()),
    path('produto/<int:pk>', ProdutoDetailDeleteUpView.as_view()),
    path('produto-estoque/<int:pk>', ProdutoUpdateEstoqueView.as_view()),
    path('vendas', VendasListCreateView.as_view())

]