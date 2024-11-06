from fastapi import APIRouter, status, HTTPException

from src.database import get_engine
from src.models import Livro
from sqlmodel import Session, select

router = APIRouter()

# Rota para pesquisar livros e por filtro de genero e ano de publicação
@router.get('', status_code=status.HTTP_200_OK)
def lerLivros(genero: str | None = None, ano: int | None = None):
    session = Session(get_engine())

    statement = select(Livro)

    if genero:
        statement = statement.where(Livro.genero == genero)

        livros = session.exec(statement).all()
        return livros
    
    elif ano:
        statement = statement.where(Livro.ano == ano)

        livros = session.exec(statement).all()
        return livros
    
    else:
        return session.exec(statement).all()
    
# Rota para adicionar um novo livro
@router.post('', status_code=status.HTTP_201_CREATED)
def adicionarLivro(livro: Livro):
    
    livro = Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        genero=livro.genero,
        ano=livro.ano,
        pais=livro.pais,
        num_paginas=livro.num_paginas
    )

    session = Session(get_engine())
    session.add(livro)
    session.commit()
    session.refresh(livro)
    
    return livro

# Rota para atualizar um livro existente
@router.put('/{id}', status_code=status.HTTP_200_OK)
def atualizarLivro(id: int, livro: Livro):
    session = Session(get_engine())

    statement = select(Livro)

    if not session.exec(statement.where(Livro.id == id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Livro não encontrado com id = {id}'
        )
    elif session.exec(statement.where(Livro.id == id)):
        session.query(Livro).update({
            Livro.titulo: livro.titulo,
            Livro.autor: livro.autor,
            Livro.genero: livro.genero,
            Livro.ano: livro.ano,
            Livro.pais: livro.pais,
            Livro.num_paginas: livro.num_paginas
        })
        session.commit()
        
        return {"detail": "Livro atualizado com sucesso"}
    
# Rota para deletar um livro
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deletarLivro(id : int, livro : Livro):
    session = Session(get_engine())

    statement = select(Livro)
    
    if not session.exec(statement.where(Livro.id == id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Livro não encontrado com id = {id}'
        )
    
    elif session.exec(statement.where(Livro.id == id)):
        session.delete(Livro)
        session.commit()
        
        return {"detail": "Livro deletado com sucesso"}

# Rota para detalhar um livro
@router.get('/{id}', status_code=status.HTTP_200_OK)
def detalharLivro(id : int):
    session = Session(get_engine())

    statement = select(Livro)
    
    if not session.exec(statement.where(Livro.id == id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Livro não encontrado com id = {id}'
        )
    
    else:
        livro = session.exec(statement.where(Livro.id == id)).first()
        
        return livro


