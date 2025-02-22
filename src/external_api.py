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
