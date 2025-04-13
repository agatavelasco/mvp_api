from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "MVP API",
        "description": "API para gerenciamento de tarefas",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"]
}

Swagger(app, config=swagger_config, template=swagger_template)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Criar uma nova tarefa
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Ler 10 páginas de um livro
    responses:
      201:
        description: Tarefa criada com sucesso
    """
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'done': new_task.done}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Listar todas as tarefas
    ---
    responses:
      200:
        description: Lista de tarefas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              done:
                type: boolean
    """
    tasks = Task.query.all()
    result = [{'id': t.id, 'title': t.title, 'done': t.done} for t in tasks]
    return jsonify(result)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_task_done(task_id):
    """
    Marcar tarefa como concluída
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa a ser marcada como concluída
    responses:
      200:
        description: Tarefa atualizada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            done:
              type: boolean
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Deletar uma tarefa
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa a ser deletada
    responses:
      200:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarefa deletada com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
