from sqlmodel import create_engine, SQLModel

#Criando o nosso Banco de Dados SQLite e onde ele ficará armazenado

#
def getEngine():
    return create_engine("sqlite:///tasks.db")

def initDB():
    return SQLModel.metadata.create_all(getEngine())