def filter_by_currency(transactions, currency):
    """функция возвращает словарь с нужным типов валюты"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """функция возвращает описание операции"""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, stop):
    """функция генерирует номера карт"""
    for num in range(start, stop + 1):
        card_number = f'{num:016}'
        formatted_card_number = f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
        yield formatted_card_number
