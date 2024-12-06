import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    last_name = Column(String(40))
    password = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)

    favorites = relationship('Favorites', back_populates='user')

class Gender(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'
    NOT_APPLICABLE = 'n/a'
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    birth_year = Column(String(20))
    gender = Column(Enum(Gender))
    height = Column(Integer)
    skin_color = Column(String(20))
    eye_color = Column(String(20))

    favorites = relationship('Favorites', back_populates='character')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    climate = Column(String(20))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

    favorites = relationship('Favorites', back_populates='planet')

class Nature(enum.Enum):
    CHARACTER = 'character'
    PLANET = 'planet'

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='favorites')
    chatacter = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
