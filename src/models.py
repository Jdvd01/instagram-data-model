import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True)

    post = relationship("post")
    seguidos = relationship("seguidos")
    seguidores = relationship("seguidores")

    user = Column(String(20), nullable = False, unique = True)
    email = Column(String(40), nullable = False, unique = True)
    password = Column(String(15), nullable = False, unique = False)
    nombre = Column(String(20), nullable = False, unique = False)
    apellido = Column(String(20), nullable = True)

class Seguidos(Base):
    __tablename__ = "seguidos"
    id = Column(Integer, primary_key = True)

    usuario = relationship("usuario")
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    seguido_id = Column(Integer, nullable = False, unique = True)


class Seguidores(Base):
    __tablename__ = "seguidores"
    id = Column(Integer, primary_key = True)

    usuario = relationship("usuario")
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    seguidore_id = Column(Integer, nullable = False, unique = True)



class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)

    usuario = relationship("usuario")
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    comentario = relationship("comentario")
    comentario_id = Column(Integer, ForeignKey("comentario.id"))

    me_gusta = relationship("me_gusta")
    me_gusta_id = Column(Integer, ForeignKey("me_gusta.id"))

    guardado = relationship("guardado")
    guardado_id = Column(Integer, ForeignKey("guardado.id"))

    descripcion = Column(String(160), nullable = False, unique = False)

    ####################################################
    # No estoy seguro de que tipo de dato lleva imagen #
    ####################################################
    imagen = Column(String(1), nullable = False, unique = False)

class Comentario(Base):
    __tablename__ = "comentario"
    id = Column(Integer, primary_key = True)

    post = relationship("post")

    mensaje = Column(String(160), nullable = False, unique = False)
    
class MeGusta(Base):
    __tablename__ = "me_gusta"
    id = Column(Integer, primary_key = True)

    post = relationship("post")
    

class Guardado(Base):
    __tablename__ = "guardado"
    id = Column(Integer, primary_key = True)

    post = relationship("post")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e