from django.contrib import admin
from Rest.models import Categoria, Produto, Titulo, Venda
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','quantidade','categoria','titulo')
    search_fields = ('preco','categoria','titulo')
    list_filter = ('categoria','titulo')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display =('cliente', 'produtos', 'valor_total')
    search_fields=('cliente', 'produtos')
    list_display=('cliente','produtos')

