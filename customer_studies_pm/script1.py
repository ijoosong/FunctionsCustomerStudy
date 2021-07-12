import requests

POKEMON_NAME = 'articuno'

def run():
    pokemon_types = get_pokemon_types(POKEMON_NAME)
    pokemon_weaknesses = get_pokemon_weaknesses(pokemon_types)
    print(pokemon_weaknesses)
    return pokemon_weaknesses
    
def get_pokemon_types(pokemon_name):
    pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    pokemon_data = pokemon_response.json()
    types_for_pokemon = []
    for type in pokemon_data['types']:
        types_for_pokemon.append(type['type']['name'])
    return types_for_pokemon

def get_pokemon_weaknesses(pokemon_types):
    types_pokemon_double_damage_from = set()
    types_pokemon_half_damage_from = set()
    types_pokemon_no_damage_from = set()

    for type in pokemon_types:
        type_response = requests.get(f'https://pokeapi.co/api/v2/type/{type}')
        type_response_json = type_response.json()
        types_pokemon_double_damage_from.update(type['name'] for type in type_response_json['damage_relations']['double_damage_from'])
        types_pokemon_half_damage_from.update(type['name'] for type in type_response_json['damage_relations']['half_damage_from'])
        types_pokemon_no_damage_from.update(type['name'] for type in type_response_json['damage_relations']['no_damage_from'])

    types_pokemon_double_damage_from = types_pokemon_double_damage_from - types_pokemon_half_damage_from
    types_pokemon_double_damage_from = types_pokemon_double_damage_from - types_pokemon_no_damage_from
    
    pokemon_weaknesses = {
        'name': POKEMON_NAME,
        'weaknesses': list(types_pokemon_double_damage_from),
        'resistances': list(types_pokemon_half_damage_from),
        'no_damage_from': list(types_pokemon_no_damage_from)
    }
    return pokemon_weaknesses

if __name__ == "__main__":
    run()