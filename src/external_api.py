import requests
API_KEY = 'bd047addbf603cdd539fc2619922cff5'




def convert_currency(transactions):
    """функция конвертации валют в рубли"""
    url = 'https://api.exchangeratesapi.io/v1/latest'

    for i in transactions:
        exchange_transaction = []
        currency_code = i.get('operationAmount',{}).get('currency',{}).get('code')
        amount = float(i.get('operationAmount', {}).get('amount'))

        if currency_code == 'RUB':
            exchange_transaction.append(amount)

        params = {'access_key': API_KEY,
                  'amount': amount,
                  'from': currency_code,
                  'to': 'RUB'}

        result = requests.get(url, params=params)

        if result.status_code == 200:
            data = result.json()

            if 'rates' in data and 'RUB' in data['rates']:
                exchange_rate = data['rates']['RUB'] * amount
                exchange_transaction.append(exchange_rate)
    return exchange_transaction


print(convert_currency( [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]))