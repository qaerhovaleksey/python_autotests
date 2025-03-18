import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '666cd890eaa1fa867d1f9b6259024452'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = 22568
NAME_TRAINER = 'Lu Kang'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200 

def test_name_trainer(): 
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Lu Kang'

CASES = [
    (22568, 'Lu Kang'), 
    (34618, 'Артем')
]


@pytest.mark.parametrize('tr_id, name', CASES)
def test_parametrize(tr_id, name):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : tr_id})
    assert response_parametrize.json()['data'][0]['trainer_name'] == name, 'Assert message'
    assert response_parametrize.status_code == 200 