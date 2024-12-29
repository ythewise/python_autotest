import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '85278f07fbd459074b48a032c4dba0e6'
Header = {
    'Content-Type': 'application/json',
    'trainer_token': Token
}

Body_create = {
    "name": "4enyxa",
    "photo_id": 9
}

response_create = requests.post(url=f'{URL}/pokemons', headers=Header, json=Body_create)
print(response_create.json())


pokemon_id = int(response_create.json()['id'])

body_update = {
    "pokemon_id": str(pokemon_id),
    "name": "Chill Guy",
    "photo_id": 2
}

response_update = requests.put(url=f'{URL}/pokemons', headers=Header, json=body_update)
print(response_update.json())


add_body = {
    "pokemon_id": str(pokemon_id)
}

add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=Header, json=add_body)
print(add_pokeball.json())
