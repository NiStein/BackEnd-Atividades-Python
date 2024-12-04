from sqlmodel import SQLModel , Field

#Criando os modelos de classe para as Tasks e de Usuário

#Criando o modelo de Classe das Tasks
class Task(SQLModel, table = True):
    id: int | None = Field(default=None,primary_key = True)
    title: str
    description: str
    status: bool = False 
    dueDate: str

#Criando o modelo de Classe dos Usuários
class User(SQLModel, table = True):
    id: int | None = Field(default=None,primary_key = True)
    name: str
    email: str
    username: str
    password: str
