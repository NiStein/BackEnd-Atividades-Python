from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from src.models import Task
from src.database import getEngine
#Aqui definiremos a nossas rotas para executar os comandos

#Definidando a instancia de rotas
router = APIRouter()

# Rota para listar todas as Tasks cadastradas
@router.get('', status_code= status.HTTP_200_OK)
def tasksList():
    session = Session(getEngine())
    sttm = select(Task)

    tasks = session.exec(sttm).all()
    return tasks
    
# Rota para listar uma Task pelo ID indicado
@router.get('/task_ID', status_code= status.HTTP_200_OK)
def taskListById(taskId : int, task: Task):
    session = Session(getEngine())
    
    sttm = select(Task)

    if not session.exec(sttm.where(Task.id == taskId)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task não encontrada com id = {taskId}'
        )
    else:
        task = session.exec(sttm.where(Task.id == taskId)).first()
        return task

# Rota para adicionar uma nova Task
@router.post('', status_code= status.HTTP_201_CREATED)
def taskAdd(task: Task):

    task = Task(
        title = task.title,
        description = task.description,
        dueDate = task.dueDate
    )
    session = Session(getEngine())
    session.add(task)
    session.commit()
    session.refresh(task)

    return 'Task adicionada com sucesso!'

# Rota para deletar um livro pelo ID
@router.delete('',status_code=status.HTTP_200_OK)
def taskDelete(taskId : int):
    session = Session(getEngine())
    
    sttm = select(Task)
    
    if not session.exec(sttm.where(Task.id == taskId)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task não encontrada com id = {taskId}'
        )
    
    else:
        session.delete(Task)
        session.commit()
        return 'Task deletada com sucesso!'
