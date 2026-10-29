from flask_app.config.mysqlconnection import connectToMySQL

class Curso:
    BASE_DATOS = "esquema_estudiantes_cursos"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = []  # Lista para guardar los estudiantes de este curso (Relación Uno a Muchos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query)
        cursos = []
        for curso in resultados:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, formulario)

    @classmethod
    def get_by_id_con_estudiantes(cls, data):
        # Esta consulta trae el curso y hace un LEFT JOIN con estudiantes para la relación uno a muchos
        query = "SELECT * FROM cursos LEFT JOIN estudiantes ON cursos.id = estudiantes.cursos_id WHERE cursos.id = %(id)s;"
        resultado = connectToMySQL(cls.BASE_DATOS).query_db(query, data)
        
        if not resultado:
            return None

        curso = cls(resultado[0])
        for row in resultado:
            # Si el estudiante existe (tiene ID en la tabla derecha)
            if row['estudiantes.id'] is not None:
                datos_estudiante = {
                    "id": row['estudiantes.id'],
                    "nombre": row['estudiantes.nombre'],
                    "apellido": row['estudiantes.apellido'],
                    "edad": row['edad'],
                    "created_at": row['estudiantes.created_at'],
                    "updated_at": row['estudiantes.updated_at'],
                    "cursos_id": row['cursos_id']
                }
                from flask_app.models.estudiante import Estudiante
                curso.estudiantes.append(Estudiante(datos_estudiante))
        return curso