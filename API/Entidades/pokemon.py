from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tabela de ligação entre Pokemon e Equipe para representar a relação muitos-para-muitos
pokemon_equipe_association = Table('pokemon_equipe_association', Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('Pokemon.id')),
    Column('equipe_id', Integer, ForeignKey('Equipe.id'))
)

class Pokemon(Base):
    __tablename__ = 'Pokemon'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    nivel = Column(Integer)
    nature = Column(String)

    # Relação muitos-para-muitos entre Pokemon e Equipe
    equipes = relationship('Equipe', secondary=pokemon_equipe_association, back_populates='pokemons')

