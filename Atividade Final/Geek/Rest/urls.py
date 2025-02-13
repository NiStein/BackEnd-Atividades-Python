from django.urls import path, include, re_path
from Rest.views import CategoriaListCreateView, TituloListCreateView, ProdutoListCreateView
from Rest.views import ProdutoUpdateEstoqueView, ProdutoDetailDeleteUpView, VendasListCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'vendas', VendasListCreateView)

urlpatterns = [
    path('categoria', CategoriaListCreateView.as_view()),
    path('titulo', TituloListCreateView.as_view()),
    path('produto', ProdutoListCreateView.as_view()),
    path('produto/<int:pk>', ProdutoDetailDeleteUpView.as_view()),
    path('produto-estoque/<int:pk>', ProdutoUpdateEstoqueView.as_view()),
    path('', include(router.urls)),
]