from sqlalchemy import Column, string, Integer
from sqlalchemy import relationship
from database import Base

class Estudande(base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(string,)
    email = Column(string,)
    perfil = relationship("Perfil", back_populates="estudante", uselist=False, cascade="all, delete-orphan")

class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(string,)
    idade = Column(String)
    endereco = Column(String)
    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'),
        unique=True
    )
    estudante = relationship(
        "Estudante",
        back_populates="perfil")