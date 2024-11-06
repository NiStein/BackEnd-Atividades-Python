# Organize o código de acordo com o visto em sala de aula em Models, Controllers, Database e Main
# Use Banco de Dados SQL. 
# Sugestão: Tente conectar com BD postgreSQL

from fastapi import FastAPI
from sqlmodel import SQLModel
from .booksControllers import router as livros_router
from .database import get_engine

app = FastAPI()

# Registrando os routers (Controllers)
app.include_router(livros_router, prefix='/livros')

# Criando DB
SQLModel.metadata.create_all(get_engine())