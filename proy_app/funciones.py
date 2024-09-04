from pony.orm import db_session
from .conex import Usuario, Paciente

@db_session
def verificar_credenciales(username, password):
    user = Usuario.get(username=username, password=password)
    return user is not None

@db_session
def añadir_paciente(nombre_paciente, apellido_paciente, enfermedad_paciente):
    try:
        nuevo_paciente = Paciente(nombre=nombre_paciente, apellido=apellido_paciente, enfermedad=enfermedad_paciente)
        return f"Paciente añadido: {nuevo_paciente.nombre} {nuevo_paciente.apellido}"
    except Exception as e:
        return f"Error al añadir paciente: {e}"

@db_session
def test_connection():
    try:
        #nuevo_paciente = Paciente(nombre_paciente="Juan", apellido_paciente="Pérez", enfermedad_paciente="Gripe")
        return "Conexión exitosa"
    except Exception as e:
        return f"Error al conectar a la base de datos: {e}"

    

