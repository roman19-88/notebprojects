import json
import os
from unittest.mock import mock_open, patch

from src.utils import operations_finances  # Импортируем вашу функцию

"""тесты для функции по открытию json-файла """


# Тест, когда файл содержит данные
@patch('builtins.open', new_callable=mock_open,
       read_data='[{"id": 1, "amount": 100, "currency": "USD"}, {"id": 2, "amount": 200, "currency": "EUR"}]')
def test_operations_finances_success(mocked_open):
    # Пример данных, которые вернет json.load
    # Мокаем json.load внутри функции
    with patch('json.load') as mock_json_load:
        mock_json_load.return_value = [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"}
        ]

        file_name = "operations.json"

        # Проверяем вызов функции
        result = operations_finances(file_name)

        # Проверяем, что данные правильно возвращаются
        assert result == [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"}
        ]

        # Получаем фактический путь так же, как в функции
        dir_name = os.path.dirname(os.path.abspath(os.path.join(file_name, '../src')))
        expected_path = os.path.join(dir_name, "src", "..", "data", file_name)
        print(f"Expected path: {expected_path}")  # Для диагностики
        print(f"Actual call args: {mocked_open.call_args}")  # Для диагностики

        # Проверяем, что open был вызван
        mocked_open.assert_called_once()

        # Проверяем, что json.load был вызван
        mock_json_load.assert_called_once()


# Тест, когда файл пустой
@patch('builtins.open', new_callable=mock_open, read_data='[]')  # Мокаем open с пустым содержимым
def test_operations_finances_empty_file(mocked_open):
    # Мокаем json.load
    with patch('json.load') as mock_json_load:
        mock_json_load.return_value = []

        file_name = "empty_transactions.json"

        result = operations_finances(file_name)

        # Проверяем, что результат пустой
        assert result == []

        # Получаем фактический путь так же, как в функции
        dir_name = os.path.dirname(os.path.abspath(os.path.join(file_name, '../src')))
        expected_path = os.path.join(dir_name, "src", "..", "data", file_name)
        print(f"Expected path: {expected_path}")  # Для диагностики
        print(f"Actual call args: {mocked_open.call_args}")  # Для диагностики

        # Проверяем, что open был вызван
        mocked_open.assert_called_once()

        # Проверяем, что json.load был вызван
        mock_json_load.assert_called_once()


# Тест, когда возникает ошибка JSONDecodeError
@patch('builtins.open', new_callable=mock_open, read_data='{invalid_json')  # Мокаем open с неправильным JSON
def test_operations_finances_json_decode_error(mocked_open):
    # Мокаем json.load для симуляции ошибки
    with patch('json.load') as mock_json_load:
        mock_json_load.side_effect = json.JSONDecodeError("Expecting value", "", 0)

        file_name = "invalid_json_transactions.json"

        result = operations_finances(file_name)

        # Проверяем, что результат пустой, так как произошла ошибка
        assert result == []

        # Получаем фактический путь так же, как в функции
        dir_name = os.path.dirname(os.path.abspath(os.path.join(file_name, '../src')))
        expected_path = os.path.join(dir_name, "src", "..", "data", file_name)
        print(f"Expected path: {expected_path}")  # Для диагностики
        print(f"Actual call args: {mocked_open.call_args}")  # Для диагностики

        # Проверяем, что open был вызван
        mocked_open.assert_called_once()

        # Проверяем, что json.load был вызван
        mock_json_load.assert_called_once()
