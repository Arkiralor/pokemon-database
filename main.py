from functions import add_pokemon_from_csv, write_to_csv, write_to_json, write_to_indv_json
from database.methods import retrieve_all, retrieve_by_id, retrieve_by_name, retrieve_type, update_by_id
import json


def main():
    '''
    Entry Point:
    '''
    # add_pokemon_from_csv()
    # output = retrieve_by_id(29)
    # output = retrieve_by_id(85)
    # output = retrieve_by_name('Nidoran')
    
    # poke_type = 'rock'
    # output = retrieve_type(poke_type)
    # request_return = write_to_csv(output, type)
    
    output = retrieve_all()
    request_return = write_to_json(inp=output, filename='all_pokemon_002.json')
    # request_return = write_to_indv_json(inp=output)

    ## To update pokemon from individual json files: 
    # output = update_by_id(id=29, src='update/29.json')
    # print(output)

    # output = update_by_id(id=32, src='update/32.json')
    # print(output)

    # meme = output[5]['abilities']
    # print(meme)
    # meme_2 = type(meme)
    # print(meme_2)

    print(request_return)

if __name__ == "__main__":
    main()
