import requests

API_KEY = 'b5293d52a016f02ea9adc610f43d8076'


def convert_currency(transactions):
    """функция конвертации валют в рубли"""
    url = 'https://api.exchangeratesapi.io/v1/latest'

    for i in transactions:
        exchange_transaction = []
        currency_code = i.get('operationAmount', {}).get('currency', {}).get('code')
        amount = float(i.get('operationAmount', {}).get('amount'))

        if currency_code == 'RUB':
            return float(amount)

        print(currency_code)
        params = {'access_key': API_KEY, 'from': currency_code, 'to': 'RUB', 'amount': amount}
        result = requests.get(url, params=params)
        print(result.url)
        print(result.status_code)
        if result.status_code == 200:
            data = result.json()
            print(data)
            if 'rates' in data and 'RUB' in data['rates']:
                exchange_rate = data['rates']['RUB'] * amount
                exchange_transaction.append(exchange_rate)
    return exchange_transaction


print(convert_currency([{
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
}]))
