from fastapi import APIRouter, HTTPException, status, Response, Depends
from sqlmodel import Session, select
from src.models import Task, CreateTaskRequest, User
from src.database import getEngine

from src.auth_utils import getLoggedUser
from typing import Annotated
#Aqui definiremos a nossas rotas para executar os comandos

#Definidando a instancia de rotas
router = APIRouter()

# Rota para listar todas as Tasks cadastradas
@router.get('', status_code= status.HTTP_200_OK)
def tasksList():
    with Session(getEngine()) as session:
        sttm = select(Task)

        tasks = session.exec(sttm).all()
        return tasks
        
# Rota para listar uma Task pelo ID indicado
@router.get('/taskID', status_code= status.HTTP_200_OK)
def taskListById(taskID : int):
    with Session(getEngine()) as session:
    
        sttm = select(Task)
        if not session.exec(sttm.where(Task.id == taskID)):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task não encontrada com id = {taskID}'
            )
        else:
            task = session.exec(sttm.where(Task.id == taskID)).first()
            return task

# Rota para adicionar uma nova Task
@router.post('', response_model=Task, status_code= status.HTTP_201_CREATED)
def taskAdd(task : CreateTaskRequest , user: Annotated[User, Depends(getLoggedUser)]):
    validTask = Task.model_validate(task)
    validTask.owner = user.id

    with Session(getEngine()) as session:
        existTask = session.exec(select(Task).where(
            Task.title == validTask.title,
            Task.owner == user.id
        ))
        if existTask:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Essa tarefa já existe')
        session.add(validTask)
        session.commit()
        session.refresh(validTask)
        return validTask

# Rota para deletar um livro pelo ID
@router.delete('/{taskID}',status_code=status.HTTP_200_OK)
def taskDelete(taskID : int, user: Annotated[User, Depends(getLoggedUser)]):
    with Session(getEngine()) as session:
    
        sttm = select(Task).where(Task.id == taskID, Task.owner == user.id)
        task = session.exec(sttm).first()
    
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task não encontrada com id = {taskID}'
            )
    
        session.delete(task)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# Rota para atualizar um livro pelo ID
@router.put('{taskID}', status_code= status.HTTP_200_OK)
def taskMarkDone(taskID : int, user: Annotated[User, Depends(getLoggedUser)]):
    with Session(getEngine()) as session:

        sttm = select(Task).where(Task.id == taskID, Task.owner == user.id)
        task = session.exec(sttm).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task não encontrada com id = {taskID}'
            )
        
        task.done = True
        session.add(task)
        session.commit()
        session.refresh(task)
        return task