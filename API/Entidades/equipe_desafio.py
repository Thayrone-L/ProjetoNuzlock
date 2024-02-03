from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EquipeDesafio(Base):
    __tablename__ = 'EquipeDesafio'

    id = Column(Integer, primary_key=True)

    # Relação muitos-para-um entre EquipeDesafio e Desafio
    desafio_id = Column(Integer, ForeignKey('Desafio.id'))
    desafio = relationship('Desafio', back_populates='equipes')

    # Relação muitos-para-um entre EquipeDesafio e Equipe
    equipe_id = Column(Integer, ForeignKey('Equipe.id'))
    equipe = relationship('Equipe', back_populates='desafios')