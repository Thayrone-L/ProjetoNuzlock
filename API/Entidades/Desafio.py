from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Desafio(Base):
    __tablename__ = 'Desafio'

    id = Column(Integer, primary_key=True)
    versao_jogo = Column(String)
    insignias_conquistadas = Column(Integer)
    # Adicione mais campos conforme necessário

    # Relação muitos-para-um entre Desafio e Usuario
    usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    usuario = relationship('Usuario', back_populates='desafios')