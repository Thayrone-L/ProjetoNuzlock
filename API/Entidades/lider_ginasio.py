from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LiderGinasio(Base):
    __tablename__ = 'LiderGinasio'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    versao_jogo = Column(String)
    link_imagem = Column(String)

    # Relação um-para-muitos entre LiderGinasio e Desafio
    desafios = relationship('Desafio', back_populates='lider_ginasio')

    # Relação muitos-para-muitos entre LiderGinasio e Pokemon
    pokemons = relationship('PokemonLiderGinasio', back_populates='lider_ginasio')

class PokemonLiderGinasio(Base):
    __tablename__ = 'PokemonLiderGinasio'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    nivel = Column(Integer)
    nature = Column(String)
    link_imagem = Column(String)

    # Relação muitos-para-um entre PokemonLiderGinasio e LiderGinasio
    lider_ginasio_id = Column(Integer, ForeignKey('LiderGinasio.id'))
    lider_ginasio = relationship('LiderGinasio', back_populates='pokemons')