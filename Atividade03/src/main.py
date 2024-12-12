from fastapi import FastAPI
from .tasksController import router as tasksRouter
from .userControllers import router as userRouter
from .database import initDB

#Criando uma instância para o FastApi
app = FastAPI()

#Inclui o router de tasksController de tarefas na rota raiz
app.include_router(tasksRouter, prefix='/task')

#Inclui o router de userController de usuários na rota raiz
app.include_router(userRouter, prefix='/user')

#Inicializa o banco de dados
initDB()
