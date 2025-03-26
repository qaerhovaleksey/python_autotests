import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOU_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "YOU_@MAIL",
    "password": "YOU_PASSWORD"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "LOLO",
    "photo_id": 4
}

body_change = {
    "pokemon_id": "269264",
    "name": "LOLO",
    "photo_id": 5
}

body_in_pokeball = {
    "pokemon_id": "269264"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text) ##Регистрация 

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email',
                                      headers= HEADER, json = body_confirmation)
print(response_confirmation.text) ##Подтверждение почты 

response_create = requests.post(url = f'{URL}/pokemons',headers= HEADER, json = body_create)
print(response_create.text) ##Создать покемона 

response_change = requests.put(url = f'{URL}/pokemons',headers= HEADER, json = body_change)
print(response_change.text) ##Cменить имя покемона 

response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',
                                     headers= HEADER, json = body_in_pokeball, timeout=5)
print(response_in_pokeball.text) ##Поймать в покеболл

response_trainer_id = requests.get(url = f'{URL}/v2/trainers', headers= HEADER)

message = response_in_pokeball.json()['message']
print(message)
