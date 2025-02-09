import pytest
from typing import List, Dict
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    },
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    },
                ],
                "USD",
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    },
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    },
                ],
        ),
        (
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    },
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    },
                ],
                "EUR",
                [],
        ),
        (
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    },
                ],
                "USD",
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    },
                ],
        ),
        (
                [],
                "USD",
                [],
        ),
    ],
)
def test_filter_by_currency(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.fixture
def sample_transactions():
    """Фикстура, возвращающая пример списка транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264270,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def test_transaction_descriptions(sample_transactions):
    """Тестирует функцию transaction_descriptions."""
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    descriptions = list(transaction_descriptions(sample_transactions))  # Преобразуем генератор в список

    assert descriptions == expected_descriptions


@pytest.fixture
def card_numbers():
    """Фикстура, возвращающая список сгенерированных номеров карт."""
    return list(card_number_generator(1, 5))


def test_card_number_generator(card_numbers):
    """Тест для функции card_number_generator с использованием фикстуры."""
    expected_card_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    assert card_numbers == expected_card_numbers
