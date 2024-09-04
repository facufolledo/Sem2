from pony.orm import db_session
from .conex import Paciente

@db_session
def añadir_paciente(nombre_paciente, apellido_paciente, enfermedad_paciente):
    try:
        nuevo_paciente = Paciente(nombre_paciente=nombre_paciente, apellido_paciente=apellido_paciente, enfermedad_paciente=enfermedad_paciente)
        return f"Paciente añadido: {nuevo_paciente.nombre_paciente} {nuevo_paciente.apellido_paciente}"
    except Exception as e:
        return f"Error al añadir paciente: {e}"

@db_session
def test_connection():
    try:
        # Intenta añadir un paciente para verificar la conexión y el esquema
        nuevo_paciente = Paciente(nombre_paciente="Juan", apellido_paciente="Pérez", enfermedad_paciente="Gripe")
        return "Conexión exitosa"
    except Exception as e:
        return f"Error al conectar a la base de datos: {e}"

    

