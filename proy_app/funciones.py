import hashlib
from pony.orm import db_session
from pony.orm import select
from .conex import Usuario, Paciente

@db_session
def verificar_credenciales(username, password):
    user = Usuario.get(nombre=username, contraseña=password)
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
@db_session
def registrar_usuario(nombre, contraseña):
    # Verifica si ya existe un usuario con ese nombre
    if select(u for u in Usuario if u.nombre == nombre).first():
        return False  # Usuario ya existe
    Usuario(nombre=nombre, contraseña=contraseña)
    return True

    


