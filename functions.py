import pandas as pd
from database.methods import add_pokemon, retrieve_by_id, update_by_id
from typing import List
import json


def add_pokemon_from_csv(path: str = 'datasets/pokemon.csv'):
    '''
    Method to batch-add pokemon to the database from a CSV file:
    '''
    df = pd.read_csv(path)

    list_of_dict = df.to_dict(orient='records')

    for row in list_of_dict:
        print(f"Pokemon: {row['name']}\n")
        add_pokemon(pokemon=row)


def write_to_csv(inp: List[dict], filename: str = 'pokemon_new'):
    '''
    Method to write the list of pokemon info retrieved from the database to a CSV file:
    '''
    dataframe = pd.DataFrame(inp)
    dataframe.to_csv(f"output/{filename}.csv")
    return f"Written to file: output/{filename}.csv"


def write_to_json(inp: List[dict], filename: str = 'all_pokemon'):
    '''
    Method to write all found pokemon to a *.JSON file:
    '''
    data = {
        'pokemon': inp
    }

    with open(f'output/{filename}.json', 'wt') as file:
        json.dump(data, file, indent=4)

    return f"Data successfully written to file: output/{filename}.json"

def write_to_indv_json(inp: List[dict]):
    '''
    Method to write to individual *.JSON files for every pokemon:
    '''
    for pokemon in inp:
        with open(f"output/individual_pokemon/{pokemon['pokedex_id']}. {pokemon['name']}.json", 'wt') as file:
            json.dump(pokemon, file, indent=4)
        print(f"Data successfully written to file: output/individual_pokemon/{pokemon['pokedex_id']}. {pokemon['name']}.json")

    return(f"All files written to directory: 'output/individual_pokemon/'")



