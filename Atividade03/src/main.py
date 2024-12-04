from fastapi import FastAPI
from .tasksController import router as tasksRouter
from .database import initDB

#Criando uma instância para o FastApi
app = FastAPI()

#Inclui o router de tasksController de tarefas na rota raiz
app.include_router(tasksRouter, prefix='/tasks')

#Inicializa o banco de dados
initDB()
