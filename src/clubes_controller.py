from fastapi import APIRouter, status, HTTPException
from sqlmodel import Session, select
from .models import Clube, RequestClube
from .database import get_engine


router = APIRouter()



@router.get('',status_code=status.HTTP_200_OK)
def lista_clubes(serie: str | None = None):

    session = Session(get_engine())
    
    statement = select(Clube)
    
    if serie:
        statement = statement.where(Clube.serie == serie)
        
    clubes = session.exec(statement).all()
    
    return clubes


@router.post('', status_code=status.HTTP_201_CREATED)
def criar_clube(novo_clube:RequestClube):
    clube = Clube(nome = novo_clube.nome, serie=novo_clube.serie)
    
    session = Session(get_engine())
    session.add(clube)
    session.commit()
    session.refresh(clube)

    return clube


@router.get('/{clube_id}')
def detalhar_clube(clube_id: int):
    for clube in clubes_futebol:
        if clube.id == clube_id:
            return clube
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Clube não encontrado com id = {clube_id}'
    )
        
        
@router.put('/{clube_id}')
def alterar_clube(clube_id: int, dados: RequestClube):
    for clube in clubes_futebol:
        if clube.id == clube_id:
            clube.nome = dados.nome
            return clube
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Clube não encontrado com id = {clube_id}'
    )


@router.delete('/{clube_id}', status_code=status.HTTP_204_NO_CONTENT)
def deletar_clube(clube_id: int):
    for clube in clubes_futebol:
        if clube.id == clube_id:
            clubes_futebol.remove(clube)
            return {f'Clube removido'}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Clube não encontrado com id = {clube_id}'
    )