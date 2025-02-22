import unittest
from unittest.mock import MagicMock, patch

from src.external_api import convert_currency


@patch('src.external_api.requests.get')
def test_convert_currency_no_conversion_for_rub(mock_get):
    """Проверяем, что если валюта уже RUB, запрос не отправляется"""
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'RUB'}
        }
    }

    result = convert_currency(transaction)

    # Поскольку валюта уже RUB, функция должна вернуть исходную сумму
    assert result == 100


@patch('src.external_api.requests.get')
def test_convert_currency_no_for_rub(mock_get):
    # Для рубля запрос к API не должен отправляться
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'RUB'}
        }
    }

    result = convert_currency(transaction)

    # Поскольку валюта уже RUB, функция должна вернуть исходную сумму
    assert result == 100


@patch('src.external_api.requests.get')
def test_convert_currency_api_failure(mock_get):
    # Симулируем ошибку запроса к API (например, статус код 500)
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }

    result = convert_currency(transaction)

    # Проверяем, что функция вернет None в случае ошибки API
    assert result is None


@patch('src.external_api.requests.get')
def test_convert_currency_no_result_in_response(mock_get):
    # Симулируем успешный ответ API без поля 'result'
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}  # Нет поля 'result'
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }

    result = convert_currency(transaction)

    # Проверяем, что функция вернет None, если нет поля 'result' в ответе
    assert result is None


if __name__ == '__main__':
    unittest.main()
