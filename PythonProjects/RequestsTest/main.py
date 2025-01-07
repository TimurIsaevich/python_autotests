import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ab62156187cf63744708e1eeee718f34'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 3
}
body_fix = {
    "pokemon_id": "183913",
    "name": "Васек",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "183913"
}

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)
response_fix = requests.put(url = f'{URL}/pokemons', headers= HEADER, json= body_fix)
print(response_fix.text)
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_catch)
print(response_catch.text)