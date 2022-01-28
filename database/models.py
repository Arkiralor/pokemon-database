'''
Contains the models for the database.
'''
from decimal import Decimal
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.sql.sqltypes import ARRAY
from sqlalchemy.orm import relationship
from .database import Base


class Pokemon(Base):
    '''
    Model/Table to contain basic information for each pokemon:
    '''

    __tablename__ = 'pokemon'

    pokedex_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    japanese_name = Column(String)
    generation = Column(Integer)
    classification = Column(String)
    is_legendary = Column(Boolean)
    abilities = Column(ARRAY(item_type=String))
    type_1 = Column(String)
    type_2 = Column(String)


class Stats(Base):
    '''
    Model/Table to contain basic stats for each pokemon:
    '''

    __tablename__ = 'stats'
    stat_id = Column(Integer, primary_key=True, index=True)
    pokedex_id = Column(Integer)
    attack = Column(Integer)
    special_atk = Column(Integer)
    defense = Column(Integer)
    special_def = Column(Integer)
    hit_points = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    speed = Column(Integer)
    capture_rate = Column(Float)


class Multipliers(Base):
    '''
    Model/Table to contain the multipliers against various types for each pokemon:
    '''

    __tablename__ = 'multipliers'

    mult_id = Column(Integer, primary_key=True, index=True)
    pokedex_id = Column(Integer)
    against_bug = Column(Float)
    against_dark = Column(Float)
    against_dragon = Column(Float)
    against_electric = Column(Float)
    against_fairy = Column(Float)
    against_fight = Column(Float)
    against_fire = Column(Float)
    against_flying = Column(Float)
    against_ghost = Column(Float)
    against_grass = Column(Float)
    against_ground = Column(Float)
    against_ice = Column(Float)
    against_normal = Column(Float)
    against_poison = Column(Float)
    against_psychic = Column(Float)
    against_rock = Column(Float)
    against_steel = Column(Float)
    against_water = Column(Float)
