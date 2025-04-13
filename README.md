# 📡 MVP To-do List - Backend

Este é o backend da aplicação **MVP To-do List**, desenvolvido com **Python + Flask**, utilizando **SQLite** como banco de dados e **Flasgger** para documentação via Swagger.

A API permite:
- Criar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Deletar tarefas

Além disso, ela oferece uma interface amigável para testes via Swagger UI.

---

## 🚀 Tecnologias

- Python 3.10+
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- SQLite

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mvp-todo-list.git
cd mvp-todo-list
```

### 2. Instale as dependências

```bash
pip install flask flask_sqlalchemy flask_cors flasgger
```

### 3. Execute o servidor

```bash
python app.py
```

### 4. Acesse no navegador:

- API: [http://localhost:5000](http://localhost:5000)
- Swagger UI: [http://localhost:5000/swagger/](http://localhost:5000/swagger/)

---

## 📂 Estrutura do projeto

```
mvp-todo-list/
├── app.py              # Código principal da API Flask
├── tasks.db            # Banco de dados SQLite (criado automaticamente)
└── README.md
```

---

## 📘 Endpoints da API

### 🔸 Criar tarefa

`POST /tasks`

#### Exemplo de body:
```json
{
  "title": "Ler 10 páginas de um livro"
}
```

#### Resposta:
```json
{
  "id": 1,
  "title": "Ler 10 páginas de um livro",
  "done": false
}
```

---

### 🔸 Listar todas as tarefas

`GET /tasks`

#### Resposta:
```json
[
  {
    "id": 1,
    "title": "Estudar Flask",
    "done": false
  },
  {
    "id": 2,
    "title": "Criar README",
    "done": true
  }
]
```

---

### 🔸 Marcar tarefa como concluída

`PUT /tasks/<task_id>`

#### Exemplo:
```http
PUT /tasks/2
```

#### Resposta:
```json
{
  "id": 2,
  "title": "Criar README",
  "done": true
}
```

---

### 🔸 Deletar uma tarefa

`DELETE /tasks/<task_id>`

#### Exemplo:
```http
DELETE /tasks/1
```

#### Resposta:
```json
{
  "message": "Tarefa deletada com sucesso"
}
```

---

## 📑 Documentação interativa

A API possui documentação Swagger acessível em:

👉 [http://localhost:5000/swagger/](http://localhost:5000/swagger/)

Você pode testar todos os endpoints por ali, com corpo de requisição e parâmetros.

---
