from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Permite solicitudes desde el frontend
CORS(app, resources={r"/api/*": {"origins": "https://anidroid1184-to-do-list.netlify.app"}})

# Base de datos temporal (en memoria)
todos = [
    {"id": 1, "task": "Aprender mucho", "completed": False},
    {"id": 2, "task": "Practicar mucho", "completed": True}
]

# Obtener todas las tareas
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Crear una nueva tarea
@app.route('/api/todos', methods=['POST'])
def create_todo():
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json['task'],
        "completed": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Actualizar una tarea (completar/no completar)
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Tarea no encontrada"}), 404
    todo['completed'] = not todo['completed']
    return jsonify(todo)

# Eliminar una tarea
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Tarea eliminada"}), 200

if __name__ == '__main__':
    app.run(debug=True)
