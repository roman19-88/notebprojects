import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def convert_currency(transaction):
    """функция конвертации валют в рубли"""

    currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
    amount = float(transaction.get('operationAmount', {}).get('amount'))
    to = "RUB"

    url = f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency_code}&amount={amount}'

    if currency_code == 'RUB':
        return amount

    headers = {'apikey': API_KEY}
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        data = result.json()

        if 'result' in data:
            return data['result']


print(convert_currency({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": 'USD',
            "code": 'USD'
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}))
