from flask import Flask
app = Flask(__name__)
app.secret_key = "clave_secreta"

# Importante: aquí se deben importar los controladores para que reconozca las rutas
from flask_app.controllers import cursos
from flask_app.controllers import estudiantes