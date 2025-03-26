"""
Test example
"""
import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOU_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = 22568
NAME_TRAINER = 'YOU_NAME'

def test_status_code():
    """
    TR-1: [auto][api] Получение тренера
    """
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID}, timeout=5)
    assert response.status_code == 200, "Unexpected status code"

def test_name_trainer():
    """
    TR-2: [auto][api] Имя тренера
    """
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID}, timeout=5)
    assert response.json()["data"][0]["trainer_name"] == 'Lu Kang', "Unexpected trainer name"

CASES = [
    (22568, 'Lu Kang'),
    (34618, 'Артем')
]

@pytest.mark.parametrize('tr_id, name', CASES)
def test_parametrize(tr_id, name):
    """
    TR-3: [auto][api] Пример параметризации
    """
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': tr_id}, timeout=5)
    assert response.json()['data'][0]['trainer_name'] == name, 'Unexpected trainer name'
    assert response.status_code == 200, "Unexpected status code"
