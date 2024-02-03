from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tabela de ligação entre Equipe e Pokemon para representar a relação muitos-para-muitos
equipe_pokemon_association = Table('equipe_pokemon_association', Base.metadata,
    Column('equipe_id', Integer, ForeignKey('Equipe.id')),
    Column('pokemon_id', Integer, ForeignKey('Pokemon.id'))
)

class Equipe(Base):
    __tablename__ = 'Equipe'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    # Relação muitos-para-um entre Equipe e Desafio
    desafio_id = Column(Integer, ForeignKey('Desafio.id'))
    desafio = relationship('Desafio', back_populates='equipes')

    # Relação muitos-para-muitos entre Equipe e Pokemon
    pokemons = relationship('Pokemon', secondary=equipe_pokemon_association, back_populates='equipes')