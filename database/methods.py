from . import models
import psycopg2 as pg
from .database import SessionLocal
from .utils import rip_string
from sqlalchemy import and_, or_
import json


def add_pokemon(pokemon: dict) -> None:
    '''
    Method to add a pokemon to the tables in the database from a dictionary:
    '''
    db = SessionLocal()

    basic = models.Pokemon(
        pokedex_id=int(pokemon['pokedex_id']),
        name=pokemon['name'],
        japanese_name=pokemon['japanese_name'],
        generation=int(pokemon['generation']),
        classification=pokemon['classification'],
        is_legendary=bool(pokemon['is_legendary']),
        abilities=rip_string(pokemon['abilities']),
        type_1=pokemon['type_1'],
        type_2=pokemon['type_2']
    )

    db.add(basic)

    stats = models.Stats(
        pokedex_id=int(pokemon['pokedex_id']),
        attack=int(pokemon['attack']),
        special_atk=int(pokemon['special_atk']),
        defense=int(pokemon['defense']),
        special_def=int(pokemon['special_def']),
        hit_points=int(pokemon['hit_points']),
        weight=float(pokemon['weight']),
        height=float(pokemon['height']),
        speed=int(pokemon['speed']),
        capture_rate=float(pokemon['capture_rate'])
    )

    db.add(stats)

    multipliers = models.Multipliers(
        pokedex_id=int(pokemon['pokedex_id']),
        against_bug=float(pokemon['against_bug']),
        against_dark=float(pokemon['against_dark']),
        against_dragon=float(pokemon['against_dragon']),
        against_electric=float(pokemon['against_electric']),
        against_fairy=float(pokemon['against_fairy']),
        against_fight=float(pokemon['against_fight']),
        against_fire=float(pokemon['against_fire']),
        against_flying=float(pokemon['against_flying']),
        against_ghost=float(pokemon['against_ghost']),
        against_grass=float(pokemon['against_grass']),
        against_ground=float(pokemon['against_ground']),
        against_ice=float(pokemon['against_ice']),
        against_normal=float(pokemon['against_normal']),
        against_poison=float(pokemon['against_poison']),
        against_psychic=float(pokemon['against_psychic']),
        against_rock=float(pokemon['against_rock']),
        against_steel=float(pokemon['against_steel']),
        against_water=float(pokemon['against_water'])
    )

    db.add(multipliers)
    db.commit()

    print(pokemon)
    print('\n')


def retrieve_by_id(id: int, db=SessionLocal()):
    '''
    Method to retrieve a single pokemon from the database by it's pokedex number:
    '''
    basic = db.query(models.Pokemon).filter(
        models.Pokemon.pokedex_id == id).first()
    stats = db.query(models.Stats).filter(
        models.Stats.pokedex_id == id).first()
    mults = db.query(models.Multipliers).filter(
        models.Multipliers.pokedex_id == id).first()

    full_data = basic.__dict__
    full_data.update(stats.__dict__)
    full_data.update(mults.__dict__)

    del full_data['_sa_instance_state']
    del full_data['stat_id']
    del full_data['mult_id']

    return full_data


def retrieve_by_name(name: str, db=SessionLocal()):
    '''
    Method to retrieve a single pokemon from the database by it's name:
    '''
    basic = db.query(models.Pokemon).filter(
        models.Pokemon.name == name).first()
    stats = db.query(models.Stats).filter(
        models.Stats.pokedex_id == basic.pokedex_id).first()
    mults = db.query(models.Multipliers).filter(
        models.Multipliers.pokedex_id == basic.pokedex_id).first()

    full_data = basic.__dict__
    full_data.update(stats.__dict__)
    full_data.update(mults.__dict__)

    del full_data['_sa_instance_state']
    del full_data['stat_id']
    del full_data['mult_id']

    return full_data


def retrieve_type(type: str, db=SessionLocal()):
    '''
    Method to retrieve all pokemon from the database by their type:
    '''
    basic_list = db.query(models.Pokemon).filter(or_(
        models.Pokemon.type_1 == type.lower(), models.Pokemon.type_2 == type.lower())).all()
    return_list = []

    for pokemon in basic_list:
        stats = db.query(models.Stats).filter(
            models.Stats.pokedex_id == pokemon.pokedex_id).first()
        mults = db.query(models.Multipliers).filter(
            models.Multipliers.pokedex_id == pokemon.pokedex_id).first()

        full_data = pokemon.__dict__
        full_data.update(stats.__dict__)
        full_data.update(mults.__dict__)

        del full_data['_sa_instance_state']
        del full_data['stat_id']
        del full_data['mult_id']

        return_list.append(full_data)

    return return_list


def retrieve_all(db=SessionLocal()):
    '''
    Method to retrieve all pokemon from the database:
    '''
    basic_list = db.query(models.Pokemon).all()
    return_list = []

    for pokemon in basic_list:
        stats = db.query(models.Stats).filter(
            models.Stats.pokedex_id == pokemon.pokedex_id).first()
        mults = db.query(models.Multipliers).filter(
            models.Multipliers.pokedex_id == pokemon.pokedex_id).first()

        full_data = pokemon.__dict__
        full_data.update(stats.__dict__)
        full_data.update(mults.__dict__)

        del full_data['_sa_instance_state']
        del full_data['stat_id']
        del full_data['mult_id']

        return_list.append(full_data)

    return return_list



    '''
    Method to add pokemon from a dict; different from original 'add' method as key names are slightly different:
    '''
    basic = models.Pokemon(
        pokedex_id=int(update['pokedex_id']),
        name=update['name'],
        japanese_name=update['japanese_name'],
        generation=int(update['generation']),
        classfication=update['classfication'],
        is_legendary=bool(update['is_legendary']),
        abilities=update['abilities'],
        type_1=update['type_1'],
        type_2=update['type_2']
    )

    db.add(basic)

    stats = models.Stats(
        pokedex_id=int(update['pokedex_id']),
        attack=int(update['attack']),
        special_atk=int(update['special_atk']),
        defense=int(update['defense']),
        special_def=int(update['special_def']),
        hit_points=int(update['hit_points']),
        weight=float(update['weight']),
        height=float(update['height']),
        speed=int(update['speed']),
        capture_rate=float(update['capture_rate'])
    )

    db.add(stats)

    multipliers = models.Multipliers(
        pokedex_id=int(update['pokedex_id']),
        against_bug=float(update['against_bug']),
        against_dark=float(update['against_dark']),
        against_dragon=float(update['against_dragon']),
        against_electric=float(update['against_electric']),
        against_fairy=float(update['against_fairy']),
        against_fight=float(update['against_fight']),
        against_fire=float(update['against_fire']),
        against_flying=float(update['against_flying']),
        against_ghost=float(update['against_ghost']),
        against_grass=float(update['against_grass']),
        against_ground=float(update['against_ground']),
        against_ice=float(update['against_ice']),
        against_normal=float(update['against_normal']),
        against_poison=float(update['against_poison']),
        against_psychic=float(update['against_psychic']),
        against_rock=float(update['against_rock']),
        against_steel=float(update['against_steel']),
        against_water=float(update['against_water'])
    )

    db.add(multipliers)
    db.commit()

    return f" Updated {update['pokedex_id']}. {update['name']}."


def update_by_id(id: int, src: str, db=SessionLocal()):
    '''
    Method to update pokemon records usind the 'pokedex_id' via a precontructed json file:
    '''

    pokemon = db.query(models.Pokemon).filter(
        models.Pokemon.pokedex_id == id).first()
    new_id = pokemon.pokedex_id
    new_name = pokemon.name
    with open(src, 'r')as file:
        update = json.load(file)

    db.query(models.Stats).filter(models.Stats.pokedex_id ==
                                  new_id).delete(synchronize_session=False)
    db.query(models.Multipliers).filter(
        models.Multipliers.pokedex_id == new_id).delete(synchronize_session=False)
    db.query(models.Pokemon).filter(models.Pokemon.pokedex_id ==
                                    new_id).delete(synchronize_session=False)

    db.commit()

    add_pokemon(update)

    return f" Updated {new_id}. {new_name} from {src}."
