import json
import os
from unittest.mock import mock_open, patch

import pytest

from src.utils import operations_finances  # Импортируем вашу функцию


# Тест, когда файл содержит данные
@patch('builtins.open', mock_open(
    read_data='[{"transaction_id": 1, "amount": 100, "currency": "USD"}, {"transaction_id": 2, "amount": 200, "currency": "EUR"}]'))
@patch('json.load')  # Мокаем json.load
def test_operations_finances_success(mock_json_load, mock_open):
    # Пример данных, которые вернет json.load
    mock_json_load.return_value = [
        {"transaction_id": 1, "amount": 100, "currency": "USD"},
        {"transaction_id": 2, "amount": 200, "currency": "EUR"}
    ]

    file_name = "transactions.json"

    # Проверяем вызов функции
    result = operations_finances(file_name)

    # Проверяем, что данные правильно возвращаются
    assert result == [
        {"transaction_id": 1, "amount": 100, "currency": "USD"},
        {"transaction_id": 2, "amount": 200, "currency": "EUR"}
    ]

    # Проверяем, что open и json.load были вызваны с правильными аргументами
    mock_open.assert_called_once_with(os.path.join(os.path.dirname(__file__), '..', 'data', file_name),
                                      encoding='utf-8')
    mock_json_load.assert_called_once()


# Тест, когда файл пустой
@patch('builtins.open', mock_open(read_data='[]'))  # Мокаем open с пустым содержимым
@patch('json.load')
def test_operations_finances_empty_file(mock_json_load, mock_open):
    # Пример, когда файл пустой
    mock_json_load.return_value = []

    file_name = "empty_transactions.json"

    result = operations_finances(file_name)

    # Проверяем, что результат пустой
    assert result == []

    # Проверяем, что open и json.load были вызваны с правильными аргументами
    mock_open.assert_called_once_with(os.path.join(os.path.dirname(__file__), '..', 'data', file_name),
                                      encoding='utf-8')
    mock_json_load.assert_called_once()


# Тест, когда возникает ошибка JSONDecodeError
@patch('builtins.open', mock_open(read_data='{invalid_json'))  # Мокаем open с неправильным JSON
@patch('json.load')
def test_operations_finances_json_decode_error(mock_json_load, mock_open):
    # Симулируем ошибку при загрузке данных
    mock_json_load.side_effect = json.JSONDecodeError("Expecting value", "", 0)

    file_name = "invalid_json_transactions.json"

    result = operations_finances(file_name)

    # Проверяем, что результат пустой, так как произошла ошибка
    assert result == []

    # Проверяем, что open и json.load были вызваны с правильными аргументами
    mock_open.assert_called_once_with(os.path.join(os.path.dirname(__file__), '..', 'data', file_name),
                                      encoding='utf-8')
    mock_json_load.assert_called_once()
