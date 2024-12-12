 Atividade de Programação Web Backend - CRUD com FastAPI
#Tarefa Prática - Criar uma API para Gerenciamento de Tarefas (TODOs) 

 Objetivo
#Desenvolver uma API RESTful utilizando FastAPI, SQLModel e um banco de dados relacional (SQLite ou PostgreSQL). A API deve permitir gerenciar tarefas (TODOs) com funcionalidades de criar, listar, atualizar e excluir tarefas.

 Requisitos Funcionais

A API deve implementar os seguintes endpoints:
1. Criar uma Tarefa
Método: POST
Path: /todos/
Parâmetros do Body:
json
Copiar código
{
  "title": "string",
  "description": "string",
  "is_completed": "boolean (opcional, padrão: false)"
}


Resposta:
Status Code: 201
Exemplo de Dados de Resposta:
json
Copiar código
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Praticar criando uma API TODOs",
  "is_completed": false,
  "created_at": "2024-11-25T12:00:00"
}



2. Listar Todas as Tarefas
Método: GET
Path: /todos/
Resposta:
Status Code: 200
Exemplo de Dados de Resposta:
json
Copiar código
[
  {
    "id": 1,
    "title": "Estudar FastAPI",
    "description": "Praticar criando uma API TODOs",
    "is_completed": false,
    "created_at": "2024-11-25T12:00:00"
  },
  {
    "id": 2,
    "title": "Configurar Banco de Dados",
    "description": "Adicionar suporte ao SQLite",
    "is_completed": true,
    "created_at": "2024-11-24T10:30:00"
  }
]



3. Obter uma Tarefa por ID
Método: GET
Path: /todos/{todo_id}
Parâmetros de Path:
todo_id (integer): ID da tarefa
Resposta:
Status Code: 200
Exemplo de Dados de Resposta:
json
Copiar código
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Praticar criando uma API TODOs",
  "is_completed": false,
  "created_at": "2024-11-25T12:00:00"
}


Erro:
Status Code: 404
Exemplo de Dados de Resposta:
json
Copiar código
{
  "detail": "Tarefa não encontrada"
}



4. Atualizar uma Tarefa
Método: PUT
Path: /todos/{todo_id}
Parâmetros de Path:
todo_id (integer): ID da tarefa
Parâmetros do Body:
json
Copiar código
{
  "title": "string",
  "description": "string",
  "is_completed": "boolean"
}


Resposta:
Status Code: 200
Exemplo de Dados de Resposta:
json
Copiar código
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Atualizado para incluir novos tópicos",
  "is_completed": true,
  "created_at": "2024-11-25T12:00:00"
}



5. Excluir uma Tarefa
Método: DELETE
Path: /todos/{todo_id}
Parâmetros de Path:
todo_id (integer): ID da tarefa
Resposta:
Status Code: 204
(Sem conteúdo no corpo da resposta)
Erro:
Status Code: 404
Exemplo de Dados de Resposta:
json
Copiar código
{
  "detail": "Tarefa não encontrada"
}



Requisitos Técnicos
Estrutura do Projeto:
Arquivo principal: main.py
Modelos: Em um arquivo separado (models.py)
Controllers (rotas): Em um arquivo separado (controllers.py)
Banco de Dados:
Utilize SQLite ou PostgreSQL.
Validações:
Valide dados de entrada usando Pydantic.
Retornos Consistentes:
Sempre utilize respostas JSON no formato especificado.
Dependências Recomendadas:
FastAPI
SQLModel
Uvicorn

Critérios de Avaliação
Organização do Código:
Separação correta entre arquivos principais, modelos e rotas.
Funcionalidade:
Implementação de todos os endpoints conforme especificado.
Validação:
Tratamento adequado de erros, como IDs inexistentes ou entradas inválidas.
Qualidade:
Código limpo, bem estruturado e fácil de entender.