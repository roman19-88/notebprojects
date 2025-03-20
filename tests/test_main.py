import unittest

from main import count_transactions_by_category, filter_transaction_by_word


def test_filter_transaction_by_word():
    """Тестируем фильтрацию транзакций по ключевому слову"""
    transactions = [
        {"description": "Покупка в магазине", "amount": 100, "currency": "RUB"},
        {"description": "Перевод другу", "amount": 200, "currency": "RUB"},
        {"description": "Оплата счета", "amount": 150, "currency": "RUB"},
        {"description": "Кафе", "amount": 50, "currency": "RUB"},
        {"description": "Покупка в магазине", "amount": 75, "currency": "RUB"},
    ]

    filtered = filter_transaction_by_word(transactions, "покупка")

    assert len(filtered) == 2
    assert transactions[0] in filtered
    assert transactions[4] in filtered


def test_count_transactions_by_category():
    """Тестируем подсчет транзакций по категориям"""
    transactions = [
        {"description": "Покупка в магазине", "amount": 100, "currency": "RUB"},
        {"description": "Перевод другу", "amount": 200, "currency": "RUB"},
        {"description": "Оплата счета", "amount": 150, "currency": "RUB"},
        {"description": "Кафе", "amount": 50, "currency": "RUB"},
        {"description": "Покупка в магазине", "amount": 75, "currency": "RUB"},
    ]
    categories = ["Покупка в магазине", "Кафе"]

    counts = count_transactions_by_category(transactions, categories)

    assert counts["Покупка в магазине"] == 2
    assert counts["Кафе"] == 1
    assert len(counts) == 2


def test_empty_filter_transaction_by_word():
    """Тестируем фильтрацию при отсутствии совпадений"""
    transactions = [
        {"description": "Покупка в магазине", "amount": 100, "currency": "RUB"},
        {"description": "Перевод другу", "amount": 200, "currency": "RUB"},
        {"description": "Оплата счета", "amount": 150, "currency": "RUB"},
    ]

    filtered = filter_transaction_by_word(transactions, "недоступно")

    assert len(filtered) == 0


def test_empty_count_transactions_by_category():
    """Тестируем подсчет транзакций по пустой категории"""
    transactions = [
        {"description": "Покупка в магазине", "amount": 100, "currency": "RUB"},
        {"description": "Перевод другу", "amount": 200, "currency": "RUB"},
        {"description": "Оплата счета", "amount": 150, "currency": "RUB"},
    ]

    empty_counts = count_transactions_by_category(transactions, [])

    assert empty_counts == {}



