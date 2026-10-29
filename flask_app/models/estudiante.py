from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    BASE_DATOS = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.cursos_id = data['cursos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, cursos_id, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(cursos_id)s, NOW(), NOW());"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, formulario)