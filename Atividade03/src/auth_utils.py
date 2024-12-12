from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from typing import Annotated, Literal
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlmodel import Session, select

from src.database import getEngine
from src.models import User

# Chave secreta e algartismo para decodificar
SECRET_KEY = '02a7e6efa2d0f77fc89f1f44d73acd7bf26e5dc6f3c1f939ff5d038ea3604f23'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='signin')

async def getLoggedUser(token : Annotated[str, Depends(oauth2_scheme)]):
    # Irá pegar o Token do Request caso válido
    # e depois pegará o usuário no DB para confirmar e retorna-lo
    exception = HTTPException(status_code = 401, detail='Não autorizado.')

    try:
        username = decodeToken(token)
    except:
        raise exception
    
    if not username:
        raise exception
    
    #Pega o usuário completo no DB
    with Session(getEngine()) as session:
        sttm = select(User).where(User.username == username)
        user = session.exec(sttm).first()

        if not user:
            raise exception
        return user

#Criando o hash do Password
def hashPassword(plainPassword : str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hash = pwd_context.hash(plainPassword)
    return hash

#Verifcando o hash do Password está correto com o Hash armazenado
def verifyHash(plainPassword : str, hashedPassword : str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    correct = pwd_context.verify(plainPassword, hashedPassword)
    return correct

# JWT Token
SECRET_KEY = '02a7e6efa2d0f77fc89f1f44d73acd7bf26e5dc6f3c1f939ff5d038ea3604f23'
ALGORITHM = 'HS256'
ACCESS_EXPIRES = 30 # 30 minutos antes de expirar
REFRESH_EXPIRES = 60 * 24 * 3 # Vale 3 dias

# Gerando um token
def generateToken(sub : str, tokenType : Literal['access', 'refresh']):
    expires = datetime.now(timezone.utc)  + timedelta(minutes=REFRESH_EXPIRES)

    if tokenType == 'refresh':
        expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_EXPIRES)
    
    token = jwt.encode({'sub': sub, 'exp': expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

# Decodificando um Token
def decodeToken(token : str):
    payLoad = jwt.decode(token, SECRET_KEY, algorithm = ALGORITHM)
    return payLoad.get('sub')
