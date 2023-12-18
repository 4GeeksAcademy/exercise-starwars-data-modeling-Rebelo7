import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
   __tablename__ = 'user'
   user_id = Column(Integer, primary_key=True)
   name = Column(String, unique=True)

class Character(Base):
   __tablename__ = 'character'
   character_id = Column(Integer, primary_key=True)
   name = Column(String(250), unique=True)
   gender = Column(String(250), nullable=False)
   height = Column(String(250), nullable=False)
   mass = Column(String(250), nullable=False)
   skin_color = Column(String(250), nullable=False)
   hair_color = Column(String(250), nullable=False)
   planet_id = Column(Integer, ForeignKey('planet.planet_id'))
   planet = relationship('Planet')

class Planet(Base):
   __tablename__ = 'planet'
   planet_id = Column(Integer, primary_key=True)
   name = Column(String(250), unique=True)
   diameter = Column(String(250), nullable=False)
   climate = Column(String(250), nullable=True)
   terrain = Column(String(250), nullable=False)
   population = Column(String(250), nullable=False)
   rotation_period = Column(String(250), nullable=False)
   orbital_period = Column(String(250), nullable=False)
   characters = relationship('Character')

class Starship(Base):
   __tablename__ = 'starship'
   starship_id = Column(Integer, primary_key=True)
   name = Column(String(250), unique=True)
   model = Column(String(250), nullable=False)
   manufacture = Column(String(250), nullable=False)
   cost_in_credits = Column(String(250), nullable=False)
   length = Column(String(250), nullable=False)
   max_atmosphering_speed = Column(String(250), nullable=False)
   crew = Column(String(250), nullable=False)
   passenger = Column(String(250), nullable=False)
   character_id = Column(Integer, ForeignKey('character.character_id'))
   character = relationship('Character',)

class Favorites(Base):
  __tablename__ = 'favorites'
  character_id = Column(Integer, ForeignKey('character.character_id'), nullable=True)
  planet_id = Column(Integer, ForeignKey('planet.planet_id'), nullable=True)
  starship_id = Column(Integer, ForeignKey('starship.starship_id'), nullable=True)
  user_id = Column(Integer, ForeignKey('user.user_id'), nullable=True)

  character = relationship('Character')
  planet = relationship('Planet')
  starship = relationship('Starship')
  user = relationship('User')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
