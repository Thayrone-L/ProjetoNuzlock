from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String)  # Armazenar hash da senha, caso seja usado autenticação local
    google_id = Column(String, unique=True)  # ID do usuário no Google, para autenticação via Google
    data_criacao = Column(DateTime, server_default='CURRENT_TIMESTAMP')
    ultima_atualizacao = Column(DateTime, onupdate='CURRENT_TIMESTAMP')
    
    # Relação um-para-muitos entre Usuario e Desafio
    desafios = relationship('Desafio', back_populates='usuario')