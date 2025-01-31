# To-Do List App (Flask + React)

Aplicación full-stack para gestión de tareas con persistencia local en SQLite.

## Stack Tecnológico
- **Backend**: Python 3.10, Flask, Flask-CORS, SQLite
- **Frontend**: React 18, Axios, CSS Modules

## Requisitos Previos
- Python 3.10+
- Node.js 18+
- pip y npm instalados

## Estructura del Proyecto
to-do-list/
├── backend/
│ ├── app.py # Servidor Flask
│ ├── todos.db # Base de datos
│ └── requirements.txt # Dependencias Python
└── frontend/
├── src/
│ ├── App.js # Componente principal
│ └── App.css # Estilos
└── package.json # Dependencias JavaScript

## Ejecución Local
### Backend (Flask)
1. Crear entorno virtual:
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate  # Unix/macOS
   ```
2. Instalar dependencias:
   ```pip install -r requirements.txt
   ```


3. Iniciar servidor:
   ````flask run --port 5000
   ````


### Frontend(React)

1. Instalar depedencias:
   ````
   cd frontend
   npm install
   ````
2. Iniciar aplicación
   ````
   npm start
   ````
