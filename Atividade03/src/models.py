from datetime import date, datetime
import datetime
from sqlmodel import SQLModel , Field

# Criando os modelos de classe para as Tasks e de Usuário

# Criando o modelo básico das Tasks
class BaseTask(SQLModel):
    title: str
    description: str
    done: bool = False 
    createdAt: str = Field(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    dueDate: date

# Crinado a classe Task que herdara a base e irá se torna uma tabela
class Task(BaseTask, table = True):
    id: int = Field(default=None, primary_key = True)
    owner : int = Field(default=None, foreign_key= 'user.id')

# Criando uma classe para fazer o requerimento de criação de uma Task
class CreateTaskRequest(BaseTask):
    pass


# Criando a classe Básica do usuário
class BaseUser(SQLModel):
    name : str
    email : str
    username : str

#Criando a clase filha de BaseUser
class User(BaseUser, table = True):
    id : int = Field(default=None, primary_key= True)
    password : str

# Criando a classe para o Usuário fazer seu Sign Up
class SignUpUserRequest(BaseUser):
    password : str
    confirmPassword : str

#Criando a classe para o Usuário fazer seu Sign In
class SignInUserRequest(SQLModel):
    username : str
    password : str