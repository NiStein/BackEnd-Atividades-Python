# Atividade de Fast API
# Crie uma API para gerenciar Livros.
# Faça as Operações para:
# Listar Todos (Aplicar filtro por gênero, ano de lançamento)
# Obter Detalhes de um Livre por ID
# Atualizar Livro
# Remover Livre
# Livro tem os atributos (id, titulo, genero, ano, autor, pais, quantidade de páginas)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# Classe de Livros
class Livro(BaseModel):
    id: int | None = None
    titulo: str 
    autor: str 
    genero: str
    ano: int 
    pais: str 
    numPaginas: int 

# Criando as instancias de livros
l1 = Livro(id=1, titulo='A Hora da Estrela',autor = 'Clarisse Lispector', genero='Drama', ano=1977, pais='Brasil', numPaginas=80)
l2 = Livro(id=2, titulo='White Fang', autor='Jack London', genero='Aventura', ano=1906, pais='EUA', numPaginas=298)
l3 = Livro(id=3, titulo='Jurassic Park', autor='Michael Crichton', genero='Terror', ano=1990, pais='EUA', numPaginas=528)
l4 = Livro(id=4, titulo='Os Dois Morrem no Final', autor='Adam Silveira', genero='Young Adult', ano=2021,pais='EUA',numPaginas=416)
livros:list[Livro] = [l1,l2,l3,l4]

# Rota para pesquisar livros e por filtro de genero e ano de publicação
@app.get('/livros/')
def lerLivros(genero: str | None = None, ano: int | None = None):
    livroEncontrados =  []

    if genero:
        for livro in livros:
            if livro.genero == genero:
                livroEncontrados.append(livro)
    
    elif ano:
        for livro in livros:
            if livro.ano == ano:
                livroEncontrados.append(livro)
    
    elif not ano and not genero:
        return livros
    
    return livroEncontrados

# Rota para detalhar um livro pelo seu ID
@app.get('/livros/{id}')
def detalheLivros(id:int):
    for livro in livros:
        if livro.id == id:
            return livro
    
    raise HTTPException(status_code=404, detail=f'O livro não foi encontrado')
        
# Rotas para adicionar um novo livro
@app.post('/livros/')
def adicionarLivro(livro: Livro):
    livros.append(livro)
    return livro

# Rotas para atualizar um livro já existente
@app.put('/livros/{id}')
def atualizarLivro(id: int, livroAtual: Livro):
    for livro in livros:
        if livro.id == id:
            livro.titulo = livroAtual.titulo
            livro.autor = livroAtual.autor
            livro.genero = livroAtual.genero
            livro.ano = livroAtual.ano
            livro.pais = livroAtual.pais
            livro.numPaginas = livroAtual.numPaginas
            return livro
    
    raise HTTPException(status_code=404, detail=f'O livro não foi encontrado')

#Rota para deletar um livro da lista
@app.delete('/livros/{id}')
def deletarLivro(id: int):
    for livro in livros:
        if livro.id == id:
            livros.remove(livro)
            return {"detail": "Livro deletado com sucesso"}
        
    raise HTTPException(status_code=404, detail=f'O livro não foi encontrado')
