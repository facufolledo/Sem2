import pymysql
pymysql.install_as_MySQLdb()
from pony.orm import Database, Required, PrimaryKey

db = Database()

db.bind(
    provider='mysql',
    host='localhost',     
    user='root',      
    passwd='44200029',
    db='db_drapp'  
)
class Usuario(db.Entity):
    Id_usuario= PrimaryKey(int, auto=True)
    nombre = Required(str,unique=True)
    contraseña = Required(str)
 
class Paciente(db.Entity):
    _table_ = 'pacientes' 
    idPaciente = PrimaryKey(int, auto=True)  
    enfermedad_paciente = Required(str) 

db.generate_mapping(create_tables=True)
