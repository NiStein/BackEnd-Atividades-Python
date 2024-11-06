from sqlmodel import SQLModel, Field

# Classe de Livros
class Livro(SQLModel):
    id: int | None = None
    titulo: str 
    autor: str 
    genero: str
    ano: int 
    pais: str 
    numPaginas: int 

