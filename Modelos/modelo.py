from sqlalchemy import Column, Integer, String
from BaseDatos.basededatos import Base

class Usuarios(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    telefono = Column(String, index=True)
    correo = Column(String, index=True)