from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.curso import Curso

# Cambia o agrega esto para que la página principal sea /cursos
@app.route('/')
def index():
    return redirect('/cursos')

@app.route('/cursos')
def index_cursos():
    cursos = Curso.get_all()
    return render_template('cursos.html', cursos=cursos)

@app.route('/curso/crear', methods=['POST'])
def crear_curso():
    Curso.guardar(request.form)
    return redirect('/cursos')

@app.route('/curso/<int:id>')
def mostrar_curso(id):
    data = {"id": id}
    curso = Curso.get_by_id_con_estudiantes(data)
    return render_template('mostrar_curso.html', curso=curso)