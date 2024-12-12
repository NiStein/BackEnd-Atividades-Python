from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select
from fastapi import APIRouter, HTTPException, status, Depends

from src.models import BaseUser, User, SignUpUserRequest, SignInUserRequest
from src.database import getEngine
from src.auth_utils import generateToken, getLoggedUser, hashPassword, verifyHash
from passlib.context import CryptContext
from typing import Annotated
import jwt

router = APIRouter()

# Rota para criar um usuário válido
@router.post('/signup', response_model= BaseUser)
def signUp(userData : SignUpUserRequest):

    with Session(getEngine()) as session:
        sttm = select(User).where(User.username == userData.username)
        user = session.exec(sttm).first()

        if user:
            raise HTTPException(status_code=400, detail='Já existe um usuário com esse UserName')
        
    if userData.password != userData.confirmPassword:
        raise HTTPException(status_code=400, detail='As senhas não coincidem!')
    
    # Fazendo o hash da senha antes de salvar no DB
    hash = hashPassword(userData.password)

    user = User(email= userData.email,
                name = userData.name,
                username = userData.username,
                password = hash)
    
    with Session(getEngine()) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
# Rota para fazer o log in do usuário
@router.post('/signin')
def signIn(signInData : SignInUserRequest):
    exceptionWrongUserPassword = HTTPException(status_code=400, detail='Senha ou Usuário incorretos(s)')

    with Session(getEngine()) as session:
        # Encontrando o usuário pelo Username
        sttm = select(User).where(User.username == signInData.username)
        user = session.exec(sttm).first()

        if not user: 
            raise exceptionWrongUserPassword
        
        if not verifyHash(signInData.password , user.password): # Senha errada
            raise exceptionWrongUserPassword
        
        # Gerando Token JWT e devolvendo
        accessToken = generateToken(user.username, 'access')
        refreshToken = generateToken(user.username, 'refresh')

        return {'accessToken': accessToken, 'refreshToken' : refreshToken}
    
# Rota para verificar se o usuário está logado
@router.get('/me', response_model=BaseUser)
def me(user: Annotated[User, Depends(getLoggedUser)]):
    return user