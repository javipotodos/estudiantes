from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso

@app.route('/estudiantes/nuevo')
def nuevo_estudiante():
    # Obtenemos todos los cursos para pasarlos al <select> del HTML
    cursos = Curso.get_all()
    return render_template('nuevo_estudiante.html', cursos=cursos)

@app.route('/estudiante/crear', methods=['POST'])
def crear_estudiante():
    Estudiante.guardar(request.form)
    # Redirige a la página de cursos tal como pide el wireframe
    return redirect('/cursos')